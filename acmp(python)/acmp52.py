n = int(input())

a = n // 100000
b = n // 10000 % 10
c = n // 1000 % 10
a1 = n // 100 % 10
b1 = n // 10 % 10
c1 = n % 10

if a + b + c == a1 + b1 + c1:
    print("YES")
else:
    print("NO")
