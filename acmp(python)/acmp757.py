atoms = list(map(int, input().split()))

sum = 0
while atoms[0] >= 2 and atoms[1] >= 6 and atoms[2] >= 1:
    sum = sum + 1
    atoms[0] -= 2
    atoms[1] -= 6
    atoms[2] -= 1
print(sum)
