s, t = list(map(int, input().split()))

if s < t:
    print(t - s)
else:
    t += 12
    print(t - s)
