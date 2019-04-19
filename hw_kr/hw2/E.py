def product(a):
    if (not a):
        yield tuple()
        return

    for i in a[0]:
        for t in product(a[1:]):
            yield tuple([i]) + tuple(t)
            
            