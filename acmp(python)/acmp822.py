def side(x1, y1, x2, y2):
    side = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
    return round(side, 1)


def triangle_area(a, b, c):
    s = (a + b + c) / 2.0
    area = (s * ((s - a) * (s - b) * (s - c))) ** 0.5
    return area


x1, y1, x2, y2, x3, y3 = list(map(float, input().split()))
ab = side(x1, y1, x2, y2)
ac = side(x1, y1, x3, y3)
bc = side(x2, y2, x3, y3)
print(round(triangle_area(bc, ac, ab), 1))
print(abs(triangle_area(bc, ac, ab)))
