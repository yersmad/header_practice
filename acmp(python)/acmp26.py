import math

o1 = list(map(int, input().split()))
o2 = list(map(int, input().split()))
centres = math.sqrt(((o1[0] - o2[0]) ** 2) + ((o1[1] - o2[1]) ** 2))

if o1[2] - o2[2] < centres or centres < o1[2] + o2[2]:
    print("NO")
else:
    print("YES")
