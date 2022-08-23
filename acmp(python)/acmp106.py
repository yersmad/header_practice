number_of_coins = int(input())
coins = []

for i in range(0, number_of_coins):
    coins.append(int(input()))

x1 = 0
x2 = 0
for x in coins:
    if x == 1:
        x1 += 1
    elif x == 0:
        x2 += 1
print(min(x1, x2))
