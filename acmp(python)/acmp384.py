def fib(n):
    if n < 2:
        return 1
    p = 1
    pp = 1
    i = 3
    while i <= n:
        c = pp + p
        pp = p
        p = c
        i += 1
    return p


def gcd(a, b):
    while a * b > 0:
        if b <= a:
            a %= b
        else:
            b %= a
    return a + b


i, j = map(int, input().split())
gcd_ij = gcd(fib(i), fib(j))
print(gcd_ij % (10 ** 9))
