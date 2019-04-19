# За линией фронта
# Роберт успешно справился с вылазкой в тыл врага и раздобыл одну полоску из тетради в клетку длиной N клеток. 
# Кроме того в руки Роберта попал лист изменений этой полоски. Враг выбирал две позиции i и j и записывал между 
# ними новое сообщение (оба конца/позиции включены). При этом, если новое сообщение накладывалось на старое, то 
# старое становилось навсегда утерянным.
# Напишите программу, которая определит, сколько на полоске осталось не утерянных сообщений.

# Формат входных данных
# Первая строка содержит число N (1 ≤ N ≤ 10000) — длину клечатой полоски.

# Вторая строка содержит число K (1 ≤ K ≤ 1000) — число сообщений.

# Следующие K строк содержат пары чисел i и j (1 ≤ i ≤ j ≤ N), задающих начало и конец сообщений.

# Формат результата
# Выведите единственное число — количество не утерянных сообщений.

# Примеры
# Входные данные
# 10
# 3
# 8 10
# 2 9
# 1 3
# Результат работы
# 1

N,K = int(input()), int(input())
l = [0]*N
messages = set()

for num in range(1,K+1):
    s = input().split(' ')
    i, j = int(s[0])-1, int(s[1])-1
    l[i] = num
    l[j] = num
    messages.add(num)


print(l)

# print(messages)

result = 0

curr = l[0]

started = set()
started.add(0)

for el in l[1:]:
    if el!=0:
        if el < curr:
            messages.discard(el)
            if el in started:
                started.discard(el)
            else:
                started.add(el)
        elif el > curr:
            if curr == 0:
                if el < max(started):
                    messages.discard(el)
                elif el in messages:
                    curr = el
                started.add(el)
            else:
                messages.discard(curr)
                if el in messages:
                    curr = el
                    started.add(el)
                else:
                    started.discard(el)
                    curr = 0
        else:
            started.discard(curr)
            result+=1
            curr = 0         

print(len(messages), messages)