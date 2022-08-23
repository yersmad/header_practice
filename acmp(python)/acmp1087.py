first = str(input())
second = str(input())
rock = 1
scissors = 2
paper = 3

if first == 1 and second == 2:
    print("First")
elif first == 2 and second == 3:
    print("First")
elif first == 3 and second == 1:
    print("First")
elif first == second:
    print("Draw")
else:
    print("Second")
