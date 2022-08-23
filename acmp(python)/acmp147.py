cache = {2: 1, 1: 1, 0: 1}


def fibonacci_rec(n):
    if n in cache:
        return cache[n]
    else:
        cache[n] = fibonacci_rec(n - 2) + fibonacci_rec(n - 1)
        return cache[n]


n = int(input())
print(fibonacci_rec(n))
