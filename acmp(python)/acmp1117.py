lesson = int(input())
a = lesson * 45 + (lesson // 2) * 5 + ((lesson + 1) // 2 - 1) * 15
print(a // 60 + 9, a % 60)
