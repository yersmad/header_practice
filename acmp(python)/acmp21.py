a, b, c = list(map(int, input().split()))
if a >= b >= c:
    d = a - c
    print(d)
elif a >= c >= b:
    d = a - b
    print(d)
elif b >= a >= c:
    d = b - c
    print(d)
elif b >= c >= a:
    d = b - a
    print(d)
elif c >= a >= b:
    d = c - b
    print(d)
elif c >= b >= a:
    d = c - a
    print(d)
