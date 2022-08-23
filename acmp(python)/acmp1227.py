def factorial(n):
    x = 1
    xx = 1
    while x <= n:
        xx = x * xx
        x += 1
    return xx


n, k = list(map(int, input().split()))
combinations = factorial(n) // (factorial(k) * (factorial(n - k)))
print(combinations)
