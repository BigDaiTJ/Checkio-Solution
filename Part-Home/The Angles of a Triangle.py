from math import acos, degrees


def checkio(a, b, c):
    # 判断是否能组成三角形
    is_triangular = a + b > c and a + c > b and b + c > a
    # 是三角形则计算角度 否则 返回[0, 0, 0]
    return [compute_angle(b, c, a), compute_angle(a, c, b), compute_angle(a, b, c)] if is_triangular else [0, 0, 0]


# 用于计算三角形的角度
def compute_angle(a, b, c):
    return round(degrees(acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
