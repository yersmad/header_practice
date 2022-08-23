def even_elements_len(numb):
    i = 0
    for c in numb:
        if c == 0:
            break
        if c % 2 == 0:
            i += 1
    return i


numb = map(int, input().split())
print(even_elements_len(numb))
