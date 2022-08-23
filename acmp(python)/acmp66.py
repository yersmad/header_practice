keyboard = "qwertyuiopasdfghjklzxcvbnm"
symbol = str(input())

i = 1
for c in keyboard:
    if c == symbol:
        print(keyboard[i])
    elif symbol == "m":
        print("q")
        break
    else:
        i += 1
