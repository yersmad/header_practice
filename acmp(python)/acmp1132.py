def sequence_len(numb):
    i = 0
    for c in numb:
        if c == 0:
            break
        i += 1
    return i


numb = map(int, input().split())
print(sequence_len(numb))
