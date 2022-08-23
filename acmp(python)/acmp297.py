nums = input()

o = 0
for i in nums:
    if i in "0":
        o += 1
    if i in "6":
        o += 1
    if i in "8":
        o += 2
    if i in "9":
        o += 1
print(o)
