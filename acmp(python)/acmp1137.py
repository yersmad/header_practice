def bigger_len(numb):
    i = -1
    last_j = 0
    for j in numb:
        if j == 0:
            return i
        elif last_j < j:
            i += 1
            last_j = j


numb = list(map(int, input().split()))
print(bigger_len(numb))
