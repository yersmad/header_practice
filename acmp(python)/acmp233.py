n = int(input())
bridges = []
for c in range(0, n):
    bridge_len = int(input())
    bridges.append(bridge_len)

for i in bridges:
    n += 1
    if i <= 437:
        print("Crash ", n)
        break
    else:
        print("No crash")
