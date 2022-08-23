def is_digit(c):
    x = 0
    for i in c:
        if i.isnumeric():
            x += 1
    return x


c = list(map(str, input().split()))
print(is_digit(c))
