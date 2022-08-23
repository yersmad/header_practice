n = int(input())
binary = bin(n)[2:]

x = 0
for x in str(binary):
    if x == 1:
        x += 1
print(x)
print(binary)
