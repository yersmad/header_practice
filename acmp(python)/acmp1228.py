def is_prime(n):
    if n < 2:
        return False

    for x in range(2, n // 2 + 1):
        if n % x == 0:
            return False

    return True


nums = list(map(int, input().split()))
sum = 0

for i in nums:
    if is_prime(i):
        sum += i
print(sum)

if is_prime(sum):
    print("Yes")
else:
    print("No")
