x = input()

nils = 0
for c in x:
    if c != "1":
        nils += 1

if nils == 0:
    print("YES")
else:
    print("NO")
