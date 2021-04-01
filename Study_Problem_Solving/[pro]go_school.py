"""
등굣길 문제
Author : Donghak Park
Contact: donghark03@naver.com
"""


def solution(m, n, puddles):
    answer = 0
    dp_table = [[0] * m for _ in range(n)]

    for i in range(m):
        dp_table[0][i] = 1

    for i in range(n):
        dp_table[i][0] = 1

    for element in puddles:
        i, j = element
        dp_table[j - 1][i - 1] = -1

    dx = [0, -1]
    dy = [-1, 0]

    for i in range(1, n):
        for j in range(1, m):
            if dp_table[i][j] == -1:
                continue

            for k in range(2):
                nx, ny = i + dx[k], j + dy[k]

                if dp_table[nx][ny] != -1:
                    dp_table[i][j] += dp_table[nx][ny]

    answer = dp_table[n - 1][m - 1]
    return answer


if __name__ == "__main__":
    m = 4
    n = 3
    puddles = [[2, 2]]
    print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0)
