w, h, r = list(map(int, input().split()))
if w < r * 2 or h < r * 2:
    print("NO")
else:
    print("YES")

