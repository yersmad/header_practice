k = int(input())
# g, c, v = 0, 1, 2

res = ""
flowers = ["G", "C", "V"]
i = 0
buff = ""
while i < k:
    buff = flowers[2]
    flowers[2] = flowers[1]
    flowers[1] = buff
    buff = flowers[0]
    flowers[0] = flowers[1]
    flowers[1] = buff
    i += 1

for c in flowers:
    res += c
print(res)
