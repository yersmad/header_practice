a, b, c, t = list(map(int, input().split()))

if t <= a:
    print(t * b)
elif a < t:
    rest = (t - a) * c
    print(a * b + rest)
