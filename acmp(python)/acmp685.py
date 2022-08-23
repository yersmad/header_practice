n = list(map(int, input().split()))
s1 = [n[0], n[1], n[2]]
s2 = [n[3], n[4], n[5]]

s1.sort()
s2.sort()

money1 = s1[0] * s2[0]
money2 = s1[1] * s2[1]
money3 = s1[2] * s2[2]

print(money1 + money2 + money3)
