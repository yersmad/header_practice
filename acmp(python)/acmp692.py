def is_binary(n):
    if n == 1:
        return True
    elif n <= 0:
        return False
    while n > 2:
        if n % 2 != 0:
            return False
        n = n // 2
    return True


n = int(input())

if is_binary(n):
    print("YES")
else:
    print("NO")
