n = int(input())

sum = 0
if 0 < n:
    for x in range(1, n + 1):
        sum = sum + x
elif n < 0:
    for x in range(n, 2):
        sum = sum + x
else:
    sum = 1
print(sum)
