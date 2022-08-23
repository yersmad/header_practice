l, w, h = list(map(int, input().split()))
s = 2*(h * l + h * w)

if s % 16 == 0:
    print(s // 16)
else:
    print(s // 16 + 1)
