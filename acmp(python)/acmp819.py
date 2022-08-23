a, b, c = list(map(int, input().split()))
S = 2 * (a * b + b * c + a * c)
V = a * b * c
print(S, V)
