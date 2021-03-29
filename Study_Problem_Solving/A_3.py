def solution(n, m, x_axis, y_axis):
    x_axis.sort()
    x_axis.append(n)
    x_axis.insert(0, 0)

    y_axis.sort()
    y_axis.append(m)
    y_axis.insert(0, 0)

    x_max = 0
    y_max = 0

    for i in range(0, len(x_axis) - 1):
        if x_max < (x_axis[i + 1] - x_axis[i]):
            x_max = (x_axis[i + 1] - x_axis[i])

    for i in range(0, len(y_axis) - 1):
        if y_max < (y_axis[i + 1] - y_axis[i]):
            y_max = (y_axis[i + 1] - y_axis[i])

    return x_max * y_max


if __name__ == "__main__":
    n1, m1 = 4, 4
    x_axis1 = [1]
    y_axis1 = [3]

    print(solution(n1, m1, x_axis1, y_axis1))

    n2, m2 = 3, 4
    x_axis2 = [2]
    y_axis2 = [1, 2]

    print(solution(n2, m2, x_axis2, y_axis2))
