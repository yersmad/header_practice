n = int(input())

x = 1
sum = 0
while x <= n:
    if n % x == 0:
        sum = sum + x
    x += 1
print(sum)
