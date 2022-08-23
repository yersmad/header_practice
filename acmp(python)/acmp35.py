def calc_d(a, b):
    return 19 * a + ((b + 239) * (b + 366)) // 2


d = int(input())
for i in range(0, d):
    m, n = list(map(int, input().split()))
    print(calc_d(n, m))
