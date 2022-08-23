def gcd(a, b):
    while a * b > 0:
        if b <= a:
            a %= b
        else:
            b %= a
    return a + b


n, m = map(int, input().split())
print(n // gcd(n, m))
