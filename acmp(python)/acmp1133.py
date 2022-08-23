def sum_len(numb):
    sum = 0
    for c in numb:
        if c == 0:
            break
        sum += c
    return sum


numb = map(int, input().split())
print(sum_len(numb))
