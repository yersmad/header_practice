numb = list(map(int, input().split()))

if numb[0] % numb[1] == 0 or numb[1] % numb[0] == 0:
    print("1")
else:
    print("666")
