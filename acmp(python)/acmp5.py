n = int(input())
marks = list(map(int, input().split()))

mark_3 = []
mark_4 = []
for i in marks:
    if i % 2 == 0:
        mark_4.append(i)
    elif i % 2 != 0:
        mark_3.append(i)
print(*mark_3, sep=' ')
print(*mark_4, sep=' ')

if len(mark_3) <= len(mark_4):
    print("YES")
else:
    print("NO")
