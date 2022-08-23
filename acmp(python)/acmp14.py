def gcd(a, b):
    while a * b > 0:
        if b <= a:
            a %= b
        else:
            b %= a
    return a + b


def lcm(a, b):
    lcm = (a * b) // gcd(a, b)
    return lcm


a, b = map(int, input().split())
print(lcm(a, b))
