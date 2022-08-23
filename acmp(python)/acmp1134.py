def mean_len(numb):
    i = 0
    sum = 0
    for c in numb:
        if c == 0:
            break
        i += 1
        sum += c
    average = sum / i
    return average


numb = map(int, input().split())
print(round(mean_len(numb), 3))
