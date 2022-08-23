N = list(map(int, input().split()))
if 727 < N[0] or 94 > N[0] or 727 < N[1] or 94 > N[1] or 727 < N[2] or 94 > N[2]:
    print("Error")
else:
    list.sort(N)
    print(N[2])
