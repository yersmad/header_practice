d = 109
v, t = list(map(int, input().split()))
s = v * t

if v > 0:
    print(s - d + 1)
elif v < 0:
    print(d - s - 1)
else:
    print(d)
