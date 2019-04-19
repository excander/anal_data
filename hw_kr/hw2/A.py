
solutions = {
    'solution1': lambda x: [i*4 for i in x],
    'solution2': lambda x: [j*(i+1) for i,j in  enumerate(x)],
    'solution3': lambda x: [i for i in x if i % 3 == 0 or i % 5 == 0],
    'solution4': lambda x: [j for i in x for j in i],
    'solution5': lambda n: sorted([(z, y ,x) for x in range(3, n+1) for y in range(3, x) for z in range(3, y) if z**2 + y**2 == x**2], key = lambda t: (t[0], t[1], t[2])),
    'solution6': lambda x: [[j+i for j in x[1]] for i in x[0]], 
    'solution7': lambda x: [list(i) for i in zip(*x)],
    'solution8': lambda x: [list(map(int, i.split())) for i in x],
    'solution9': lambda x: {chr(ord('a')+i):i**2 for i in x},
    'solution10': lambda x: set(sorted(i.capitalize() for i in x if len(i)>3)),
}

