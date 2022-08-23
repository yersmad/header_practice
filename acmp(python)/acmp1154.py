ip = input()
ip = list(map(int, ip.split(".")))

x = 0
for c in ip:
    if 255 >= c >= 0:
        x += 1

if x == 4:
    print("Good")
else:
    print("Bad")
