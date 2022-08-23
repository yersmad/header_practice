t1, t2 = list(map(int, input().split()))
mode = str(input())

if mode == "freeze":
    print(min(t1, t2))
elif mode == "heat":
    print(max(t1, t2))
elif mode == "auto":
    print(t2)
else:
    print(t1)

