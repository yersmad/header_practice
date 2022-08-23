n = int(input())
n_list = list(map(int, input().split()))
x = int(input())

y = 0
for i in n_list:
    if i == x:
        y += 1
print(y)
