def calc_sum(nums):
    val = 0
    sum = 0
    for x in nums:
        val = val + x
        sum = sum + val
    return sum


n = int(input())
nums = list(map(int, input().split()))

a = calc_sum(nums)

nums.reverse()
b = calc_sum(nums)

nums.sort()
c = calc_sum(nums)

i = min(a, b, c)
if c == i:
    print(1)
elif b == i:
    print(3)
else:
    print(5)
