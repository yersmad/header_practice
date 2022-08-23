n = int(input())

a = n // 1000
b = n // 100 % 10
b1 = n // 10 % 10
a1 = n % 10

if a == a1 and b == b1:
    print("YES")
else:
    print("NO")
