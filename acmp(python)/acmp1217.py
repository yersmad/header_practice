n = int(input())
marks = list(map(int, input().split()))
updated_marks = []

for i in marks:
    if i == max(marks):
        updated_marks.append(min(marks))
    elif i != max(marks):
        updated_marks.append(i)
print(*updated_marks, sep=" ")
