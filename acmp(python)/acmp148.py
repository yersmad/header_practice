def gcd(a, b):
    while a * b > 0:
        if b <= a:
            a %= b
        else:
            b %= a
    return a + b


a, b = map(int, input().split())
print(gcd(a, b))
