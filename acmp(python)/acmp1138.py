def second_max_len(num):
    max_num = 0
    second_max_num = 0
    num_list = []
    for j in num:
        if j == 0:
            return num_list
        num_list.append(j)
        max_num = max(num_list)
        num_list.remove(max(num_list))


num = map(int, input().split())
print(second_max_len(num))
