def nils(nums):
    x = 0
    for i in nums:
        if i == 0 and nums[i] == nums[i + 1]:
            x += 1
    return x


nums = list(map(str, input().split()))
print(nils(nums))
print(nums)
