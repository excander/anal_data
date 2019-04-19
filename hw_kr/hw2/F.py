def brackets(n):
    def br(l, r, c):
        if r == n:
            yield c
        if l < n:
            yield from br(l + 1, r, c + "(")
        if r < l:
            yield from br(l, r + 1, c + ")")

    yield from br(0, 0, "")


if __name__ == "__main__":
    n = int(input())
    for i in brackets(n):
        print(i)
