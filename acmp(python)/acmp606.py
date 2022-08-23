coord = list(map(int, input().split()))

if coord[0] + coord[1] <= coord[2] or coord[0] + coord[2] <= coord[1] or coord[1] + coord[2] <= coord[0]:
    print("NO")
else:
    print("YES")
