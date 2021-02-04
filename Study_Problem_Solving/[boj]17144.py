"""
미세먼지 안녕! 문제
author : donghak park
contact: donghark03@naver.com
"""

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def check_all():
    temp = 0

    for i in range(R):
        temp += sum(arr[i])

    return temp +2


def spread():
    temp = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):

            if arr[i][j] == -1:
                continue
            else:
                x, y = i, j
                amount = arr[x][y]//5
                last = arr[x][y]

                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < R and 0 <= ny < C:
                        if arr[nx][ny] != -1:
                            temp[nx][ny] += amount
                            last -= amount
                temp[x][y] += last
    temp[air_conditional[0]][0] = -1
    temp[air_conditional[1]][0] = -1

    return temp

def clean_air(arr):

    up = air_conditional[0]
    down = air_conditional[1]


    # 1열 위쪽 아래로 내리기
    for i in range(up-1, 0, -1):
        arr[i][0] = arr[i-1][0]
    arr[0][0] = 0

    # 1열 아래쪽 위로 올리기
    for i in range(down+2, R):
        arr[i-1][0] = arr[i][0]
    arr[R-1][0] = 0

    #왼쪽으로 이동
    for i in range(0, C-1):
        arr[0][i] = arr[0][i+1]
        arr[R-1][i] = arr[R-1][i+1]
    arr[0][C-1] = 0
    arr[R-1][C-1] = 0

    # R열 위쪽 위로
    for i in range(0, up):
        arr[i][C-1] = arr[i+1][C-1]
    arr[up][C-1] = 0

    # R열 아래쪽 아래로
    for i in range(R-1, down, -1):
        arr[i][C-1] = arr[i-1][C-1]
    arr[down][C-1] =0

    #오른쪽으로 이동
    for i in range(C-1, 1, -1):
        arr[up][i] = arr[up][i-1]
        arr[down][i] = arr[down][i-1]

    arr[up][1] = 0
    arr[down][1] = 0

R, C, T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(R)]

time = 0

air_conditional = []

for i in range(R):
    if arr[i][0] == -1:
        air_conditional.append(i)

while time < T:
    arr = spread()
    clean_air(arr)
    time += 1

answer = check_all()
print(answer)
