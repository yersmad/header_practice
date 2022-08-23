n, k = list(map(int, input().split()))
one = k // n
two = k % n
three = n - two

if k % n == 0:
    print(one, two, two)
else:
    print(one, two, three)
