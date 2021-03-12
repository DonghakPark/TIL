"""
2021 상반기 코딩테스트 대비 연습 문제 풀이
Author : DongHak Park
Contact: donghark03@naver.com
"""
from itertools import combinations


def solution(line):
    answer = []
    com = list(combinations(line, 2))
    star = []
    row_len = [int(1e9), - int(1e9)]
    col_len = [int(1e9), - int(1e9)]
    for line1, line2 in com:
        a, b, e = line1
        c, d, f = line2
        if ((a * d) - (b * c)) == 0:
            continue
        else:
            x = ((b * f) - (e * d)) / ((a * d) - (b * c))
            y = ((e * c) - (a * f)) / ((a * d) - (b * c))
            if ( int(x) == float(x) ) and ( int(y) == float(y) ):
                star.append([int(x),int(y)])

                row_len[0] = min(row_len[0], x)
                row_len[1] = max(row_len[1], x)

                col_len[0] = min(col_len[0], y)
                col_len[1] = max(col_len[1], y)
    row = int(abs(row_len[0] - row_len[1]) + 1)
    col = int((abs(col_len[0] - col_len[1]) + 1))
    matrix = [[0] * row for _ in range(col)]

    for x,y in star:
        nx, ny = 0,0
        if row != 1:
            nx = row // 2 + x
        else:
            nx = 0
        if col != 1:
            ny = col // 2 + y
        else:
            ny = 0
        matrix[ny][nx] = 1

    for element in matrix:
        temp = list(map(str, element))
        temp = "".join(temp)
        temp = temp.replace("0", ".")
        temp = temp.replace("1", "*")
        answer.append(temp)

    answer.reverse()
    return answer


if __name__ == "__main__":
    line = [
        [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]],
        [[0, 1, -1], [1, 0, -1], [1, 0, 1]],
        [[1, -1, 0], [2, -1, 0]],
        [[1, -1, 0], [2, -1, 0], [4, -1, 0]]
    ]

    result = [["....*....", ".........", ".........", "*.......*",
               ".........", ".........", ".........", ".........",
               "*.......*"],
              ["*.*"],
              ["*"],
              ["*"]]

    for i in range(4):
        if solution(line[i]) == result[i]:
            print("{}번 Test_case 정답입니다.".format(i))
        else:
            print("{}번 Test_case 틀렸습니다.".format(i))
