import math

p_list = [2]
def is_prime(n):
    if n != 2 and n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_list_in_range(x, y):
    prime_list = []
    for i in range(x, y + 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list


m, n = map(int, input().split())
prime_list = prime_list_in_range(m, n)
if len(prime_list) == 0:
    print("Absent")
else:
    for i in prime_list:
        print(i)
