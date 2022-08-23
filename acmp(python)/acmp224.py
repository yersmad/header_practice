n = int(input())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
ans = 1
for i in nums[:3]:
    ans = ans * i
print(ans)
