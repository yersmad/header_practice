import math

coord = list(map(int, input().split()))
AB = math.sqrt(((coord[2] - coord[0]) ** 2) + ((coord[3] - coord[1]) ** 2))
print(AB)
