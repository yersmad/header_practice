l, u, p, d = 0, 0, 0, 0
s = str(input())
capitalalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalphabets = "abcdefghijklmnopqrstuvwxyz"
specialchar = "$@_"
digits = "0123456789"

if len(s) >= 12:
    for i in s:
        if i in smallalphabets:
            l += 1
        if i in capitalalphabets:
            u += 1
        if i in digits:
            d += 1
if l >= 1 and u >= 1 and d >= 1 and l + u + d == len(s):
    print("Yes")
else:
    print("No")
