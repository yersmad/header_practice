def print_fibonacci(n):
    p = 1
    pp = 1
    print(pp, p, end=' ')
    i = 2
    while i < n:
        c = pp + p
        print(c, end=' ')
        pp = p
        p = c
        i += 1


def fibonacci(n):
    if n < 2:
        return 1
    p = 1
    pp = 1
    i = 2
    while i <= n:
        c = pp + p
        pp = p
        p = c
        i += 1
    return p


def fibonacci_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci_rec(n - 2) + fibonacci_rec(n - 1)


cache = {1: 1, 0: 1}


def fibonacci_rec_cache(n):
    if n in cache:
        return cache[n]
    else:
        cache[n] = fibonacci_rec_cache(n - 2) + fibonacci_rec_cache(n - 1)
        return cache[n]


n = int(input())
print(fibonacci_rec_cache(n))
