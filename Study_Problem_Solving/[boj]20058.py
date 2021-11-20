"""
마법사 상어와 파이어스톰
Author: DongHak Park
"""
from collections import deque

def rotate(x_s, y_s, N_s):
    global ice_map
    global row
    temp_arr = [[0] * row for _ in range(row)]
    move = N_s//2

    #왼위 -> 오른쪽으로
    for i in range(x_s, x_s + move):
        for j in range(y_s, y_s + move):
            temp_arr[i][j+move] = ice_map[i][j]
    #위로
    for i in range(x_s + move, x_s + move * 2):
        for j in range(y_s, y_s + move):
            temp_arr[i-move][j] = ice_map[i][j]
    #아래로
    for i in range(x_s, x_s + move):
        for j in range(y_s + move, y_s + move*2):
            temp_arr[i + move][j] = ice_map[i][j]

    #왼쪽으로
    for i in range(x_s +move, x_s +move*2):
        for j in range(y_s +move, y_s +move*2):
            temp_arr[i][j - move] = ice_map[i][j]

    for i in range(x_s, x_s + move * 2):
        for j in range(y_s, y_s + move * 2):
            ice_map[i][j] = int(temp_arr[i][j])

def remove():
    global ice_map
    temp_arr = [[0] * row for _ in range(row)]

    for i in range(row):
        for j in range(row):
            x, y = i ,j
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < row and 0 <= ny < row:
                    if ice_map[nx][ny] > 0:
                        temp_arr[x][y] += 1

    for i in range(row):
        for j in range(row):
            if temp_arr[i][j] < 3 and ice_map[i][j] > 0:
                ice_map[i][j] -= 1

def BFS(x,y):
    global visited
    global second_answer

    Q = deque()
    Q.append([x,y])
    cnt = 1
    while Q:
        now_x, now_y = Q.popleft()

        for i in range(4):
            nx,ny = now_x + dx[i], now_y + dy[i]
            if 0 <= nx < row and 0 <= ny < row and visited[nx][ny] is False:
                if ice_map[nx][ny] > 0:
                    cnt += 1
                    Q.append([nx, ny])
                    visited[nx][ny] = True
    second_answer = max(second_answer, cnt)


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

N, Q = map(int, input().split())

row = (2**N)

ice_map = []

for _ in range(row):
    ice_map.append(list(map(int, input().split())))

L = list(map(int, input().split()))


for l in range(Q):

    sub_row = (2 ** L[l])
    # for i in range(0, row, sub_row):
    #     for j in range(0, row, sub_row):
    #         start_x = i
    #         start_y = j
    #         #돌리기
    #         rotate(start_x, start_y, sub_row)
    for x in range(0, row, sub_row):
        for y in range(0, row, sub_row):
            tmp = [ice_map[i][y:y+sub_row] for i in range(x, x+sub_row)]
            for i in range(sub_row):
                for j in range(sub_row):
                    ice_map[x + j][y+sub_row-1-i] = tmp[i][j]
                    print("({},{}) --> ({},{})".format(i,j,x+j, y+sub_row-1-i))
    # for element in ice_map:
    #     print(*element)
    # print("-------------------------")
    remove() #없애기

first_answer = 0
for element in ice_map:
    first_answer += sum(element)
print(first_answer)

second_answer = 0
visited = [[False] * row for _ in range(row)]

for i in range(row):
    for j in range(row):
        if ice_map[i][j] != 0:
            visited[i][j] = True
            BFS(i,j)

print(second_answer)
