def side(x1, y1, x2, y2):
    ab = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
    return ab


def is_right_triangle(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    elif a ** 2 + c ** 2 == b ** 2:
        return True
    elif b ** 2 + c ** 2 == a ** 2:
        return True
    else:
        return False


x1, y1, x2, y2, x3, y3 = list(map(int, input().split()))
points = [side(x2, y2, x3, y3), side(x1, y1, x3, y3), side(x1, y1, x2, y2)]

if is_right_triangle(points[0], points[1], points[2]):
    print("Yes")
else:
    print("No")
print(points)
