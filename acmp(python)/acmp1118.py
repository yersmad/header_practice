import math

h, a, b = list(map(int, input().split()))

days = 1 + math.ceil((h - a) / (a - b))
print(days)
