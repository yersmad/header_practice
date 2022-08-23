import string

i = str(input())

if i.islower() and i in string.ascii_letters:
    print(i.upper())
elif i.isupper() and i in string.ascii_letters:
    print(i.lower())
else:
    print(i)
