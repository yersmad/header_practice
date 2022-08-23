def max_len(numb):
    max_numb = 0
    numb_list = []
    for c in numb:
        if c == 0:
            return max_numb
        numb_list.append(c)
        max_numb = max(numb_list)


numb = map(int, input().split())
print(max_len(numb))
