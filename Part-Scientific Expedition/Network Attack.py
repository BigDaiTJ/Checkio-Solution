# 总体思路：将所有点的时间统计出来，通过访问队列来确定当前顶点是否正在被攻击，而后根据访问队列来确定是否需要进行时间的更新
def capture(matrix):
    # 记录顶点的攻破时间
    vertices = {i: matrix[i][i] for i in range(len(matrix))}
    # 记录已访问顶点
    visited = {0}
    time = 0
    # 当字典中的值均为0是停止
    while any(vertices.values()):
        # 将当前已经访问的结点进行存储 判断依据为当前行对应的列值是否为1
        for i, j in vertices.items():
            if j == 0:
                visited |= {n for n, item in enumerate(matrix[i]) if item == 1}
        # 时间每次加1
        time += 1
        # 将现在访问队列中为攻破的结点时间减1
        for i, j in vertices.items():
            if i in visited and j != 0:
                vertices[i] -= 1
    return time


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 1]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
