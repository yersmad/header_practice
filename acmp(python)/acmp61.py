a1, b1 = list(map(int, input().split()))
a2, b2 = list(map(int, input().split()))
a3, b3 = list(map(int, input().split()))
a4, b4 = list(map(int, input().split()))
if b1 + b2 + b3 + b4 < a1 + a2 + a3 + a4:
    print("1")
elif a1 + a2 + a3 + a4 < b1 + b2 + b3 + b4:
    print("2")
else:
    print("DRAW")
