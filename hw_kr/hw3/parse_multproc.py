from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import pandas as pd

import time


authors_dict = {
  "Дарья Донцова":  29369,
  "Джеймс Роллинс": 29442,
  "Макс Фрай":      102994,
  "Эрин Хантер":    26149,
  "Дмитрий Емец":   35952
}


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)


def show_pages():
    SCROLL_PAUSE_TIME = 1

    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    next_pages = None
    try:    
        next_pages = driver.find_element_by_xpath("//a[@class='ty']")
    except Exception:
        print('last page! (NoSuchElementException)')

    if next_pages is not None:
        driver.execute_script(f"window.scrollTo({next_pages.location['x']}, {next_pages.location['y']-200});")
        
        next_pages.click()
        show_pages()

def get_books_ids(l, author):
    books = driver.find_elements_by_class_name("gf")
    for book in books:
        l.append(book.get_attribute('data-book'))

book_ids = []

for author in authors_dict:
    driver.get(f"https://www.bookvoed.ru/author/books?id={authors_dict[author]}")
    show_pages()
    get_books_ids(book_ids, author)

driver.close()

############## 2 ##############

# book_ids = book_ids[:]

def extract_book_info(book_id):
    book_url = f"https://www.bookvoed.ru/book?id={book_id}"
    print(book_url)
    book_html = requests.get(book_url).text
    soup = BeautifulSoup(book_html, 'html.parser')

    age_limits = {
        'ov nM': '0+',
        'pv nM': '6+',
        'qv nM': '12+',
        'rv nM': '16+',
        'sv nM': '18+'
    }

    def parse_price(price):
        if not price:
            return ''
        else:
            price = price.text.strip()
        if price.find('.') + 1 == len(price):
            price = price.rstrip(" pуб.")
        else:
            price = price.rstrip(" pуб.")[price.find('.') + 2 : ]
        return float(price.replace(" ", ""))

    def parce_likes(num):
        return int(num) if num else 0

    def parse_description(descr):
        return descr.contents[0].strip() if descr else ""

    book_info = {
       "ID": book_id,
       "Название": soup.find('h1').contents[0].rstrip(),
       "Обложка": soup.find('img', class_ = 'tf')["src"],
       "Возраст": age_limits[' '.join(soup.find('div', class_ = 'bw').contents[3].contents[3]["class"])],
       "Описание": parse_description(soup.find('div', class_ = 'lw')),
       "Рейтинг": float(soup.find('div', class_ = 'af')["style"][7:-1]),
       "Понравилось": parce_likes(soup.find('a', class_ = 'Ke Me ').text.strip()),
       "В закладки": parce_likes(soup.find('a', class_ = 'Ke Le ff').text.strip()),
       "Не понравилось": parce_likes(soup.find('a', class_ = 'Ke Oe ').text.strip()),
       "Цена": parse_price(soup.find('div', class_ = "Hu Wu")),
       "Серия": "",
       "Издательство": "",
       "Год": "",
       "Страниц": "",
       "Переплёт": "",
       "ISBN": "",
       "Размеры": "",
       "Формат": "",
       "Код": "",
       "В базе": "",
       "Автор": "",
       "Тематика": "",
       "Тираж": ""
    }

    table = soup.find('table', class_='tw')
    rows = table.find_all('tr')
    data = [list(map(lambda x: x.text.rstrip(':'), row.find_all('td'))) for row in rows]

    for k, v in data:
        book_info[k] = v

    book_info['Год'] = int(book_info['Год']) if book_info['Год'] else ""
    book_info['Страниц'] = int(book_info['Страниц']) if book_info['Страниц'] else ""
    book_info['Код'] = int(book_info['Код']) if book_info['Код'] else ""
    book_info['Тираж'] = int(book_info['Тираж']) if book_info['Тираж'] else ""

    return book_info


from multiprocessing import Pool, Lock, Value
from time import sleep

mutex = Lock()
n_processed = Value('i', 0)


def func_wrapper(uid):
    res = extract_book_info(uid) 
    with mutex:
        global n_processed
        n_processed.value += 1
        if n_processed.value % 10 == 0:
            print(f"\r{n_processed.value} objects are processed...", end='', flush=True)
    return res

with Pool(processes=10) as pool:
    result = pool.map(func_wrapper, book_ids)


# result = list(map(extract_book_info, book_ids))
df = pd.DataFrame(result)
df.sort_values(by=['ID'], inplace=True)

with open('hw_3.csv', mode='w', encoding='utf-8') as f_csv:
    df.to_csv(f_csv, index=False)
