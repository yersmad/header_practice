h, m, s = list(map(int, input().split()))
h1, m1, s1 = list(map(int, input().split()))
seconds1 = (h * 60 * 60) + (m * 60) + s
seconds2 = (h1 * 60 * 60) + (m1 * 60) + s1
print(seconds2 - seconds1)
