# 청소년 상어

import copy

# 4*4 크기 격자에 존재하는 각 물고기의 번호( 없으면 -1 )와 방향 값을 담는 테이블
array = [ [None] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))

    #매 줄마다 4마리의 물고기를 하나식 확인하며
    for j in range(4):
        array[i][j] = [data[j*2],data[j*2+1] -1]

# 8가지 방향에 대한 정의
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def turn_left(direction):
    return (direction +1) % 8

result = 0

#현재 배열에서 특정한 번호의 물고기 위치 찾기
def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i,j)
    return None

#모든 물고기를 회전 및 이동시키는 함수
def move_all_fishes(array, now_x, now_y):
    for i in range(1,17):
        position = find_fish(array, i)
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1]

            for j in range(8):
                nx = x+dx[direction]
                ny = y+dy[direction]

                if 0<=nx and nx<4 and 0<= ny and ny <4:
                    if not (nx==now_x and ny==now_y):
                        array[x][y][1] = direction
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break

                direction = turn_left(direction)

def get_possible_position(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]

    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]

        if 0<= now_x and now_x < 4 and 0<= now_y and now_y < 4:
            if array[now_x][now_y][0] != -1:
                positions.append((now_x,now_y))

    return positions

def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)

    total += array[now_x][now_y][0]
    array[now_x][now_y][0] = -1

    move_all_fishes(array, now_x, now_y)

    positions = get_possible_position(array, now_x, now_y)

    if len(positions) == 0:
        result = max(result, total)
        return

    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)

dfs(array, 0,0,0)
print(result)