x, y, z = list(map(int, input().split()))
if x + y == z:
    print(0)
elif z < x + y:
    i = (x + y) - z
    print(i)
else:
    print("Impossible")
