import operator
import re
from functools import reduce

solutions = {
    # ['12', '25.6', '84,02', '  69-91'] -> [21, 652, 2048, 1996]
    'solution1': lambda x: list(map(lambda y: int(re.sub("[^0-9]", "", y[::-1])), x)),

    # zip(range(2, 5), range(3, 9, 2)) -> [6, 15, 28]
    'solution2': lambda x: list(map(lambda z: z[0]*z[1], x)),

    # range(20) -> [0, 2, 5, 6, 8, 11, 12, 14, 17, 18]
    'solution3': lambda x: list(filter(lambda a: (a-1) % 6 and (a-3) % 6 and (a-4) % 6, x)),

    # ['', 25, None, 'python', 0.0, [], ('msu', '1755-01-25')] -> [25, 'python', ('msu', '1755-01-25')]
    'solution4': lambda x: list(filter(lambda z: bool(z), x)),

    # rooms = [{"name": "комната1", "width": 2, "length": 4}, ... , ]
    'solution5': lambda x: list(map(lambda d: operator.setitem(d, 'square', d['width']*d['length']),  x)),
    'solution6': lambda x: list( map (lambda d: dict(zip(list(d.keys())+['square'], list(d.values()) + [d['width'] * d['length']] )), x)),

    # [{1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}, {3, 4, 5, 6, 7}] -> {3, 4, 5}
    'solution7': lambda x: set(reduce(lambda a, b: a & b, x)),

    # [1, 2, 1, 1, 3, 2, 3, 2, 4, 2, 4] -> {1: 3, 2: 4, 3: 2, 4: 2}
    'solution8': lambda x: dict(reduce(lambda a, b: operator.setitem(a, b, a.get(b, 0)+1) or a, x, {})),

    # students -> ['Alina', 'Sergey', 'Valya']
    'solution9': lambda x: list(map(lambda t: operator.getitem(t, 'name'), filter(lambda t: t['gpa'] > 4.5, x))),

    # ['165033', '477329', '631811', '478117', '475145', '238018', '917764', '394286'] -> ['165033', '475145', '238018']
    'solution10': lambda x: list(filter(lambda t: sum(map(int, list(t[::2]))) == sum(map(int, list(t[1::2]))), x)),
}