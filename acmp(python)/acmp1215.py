n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

for i in numbers:
    if i == x:
        print(i)
    elif i < x:
        print(i)
