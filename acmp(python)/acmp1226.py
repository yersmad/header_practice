def is_letter(c):
    x = 0
    for i in c:
        if i.isalpha():
            x += 1
    return x


c = list(map(str, input().split()))
print(is_letter(c))
