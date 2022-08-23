n, m, k = list(map(int, input().split()))
if n * m > k:
    print("YES")
elif n * m == k:
    print("YES")
else:
    print("NO")
