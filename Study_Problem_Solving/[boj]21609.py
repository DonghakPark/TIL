"""
상어 중학교 문제
Author : DongHak Park
"""
from collections import deque, defaultdict
import copy

def display():
    global block_map

    for element in block_map:
        print(*element)

    print("---------------------------------")

def make_group(x, y, color):
    global block_map
    global group_list

    visited = [[False] * N for _ in range(N)]

    visited[x][y] = True

    Q = deque()
    Q.append([x,y])
    local_group = [[x,y,0]]
    normal_count = 0
    while Q:
        now_x, now_y = Q.popleft()

        for i in range(4):
            nx, ny = now_x + dx[i], now_y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                if block_map[nx][ny] == color:
                    Q.append([nx,ny])
                    local_group.append([nx,ny,0])
                    visited[nx][ny] = True
                    normal_count += 1
                if block_map[nx][ny] == 0:
                    Q.append([nx,ny])
                    local_group.append([nx,ny,1])
                    visited[nx][ny] = True

    size_group = len(local_group)
    if size_group >= 2:
        local_group.sort(key=lambda x :(x[2], x[0], x[1]))
        rainbow_cnt = 0
        for element in local_group:
            if element[2] == 1:
                rainbow_cnt += 1
        a, b, c = local_group[0]
        if (size_group, rainbow_cnt, a, b) not in group_list.keys():
            group_list[(size_group, rainbow_cnt, a, b)] = local_group

def gravity():
    global block_map

    for i in range(N-1, -1, -1):
        for j in range(N):
            if block_map[i][j] != -1 and block_map[i][j] != -2:
                now_block = int(block_map[i][j])
                block_map[i][j] = -2
                now_x, now_y = i, j

                while True:
                    flag = False
                    nx, ny = now_x + 1, now_y

                    if 0 <= nx < N and 0 <= ny < N:
                        if block_map[nx][ny] == -2:
                            now_x, now_y = nx, ny
                            flag = True
                    if flag == False:
                        block_map[now_x][now_y] = now_block
                        break

def rotate():
    global block_map

    temp_arr = [[-2] * N for _ in range(N)]
    for c in range(N-1, -1, -1):
        for r in range(N-1, -1, -1):
            temp_arr[N-c-1][r] = block_map[r][c]

    block_map = copy.deepcopy(temp_arr)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

N, M = map(int, input().split())

block_map = []
for _ in range(N):
    block_map.append(list(map(int, input().split())))



answer = 0
while True:
    group_list = defaultdict(list)
    for i in range(N):
        for j in range(N):
            if block_map[i][j] >= 1:
                make_group(i, j, block_map[i][j])

    if len(group_list.keys()) == 0:
        break

    group_key = list(group_list.keys())
    group_key.sort(key=lambda x:(-x[0], -x[1], -x[2], -x[3]))
    now_group_key = group_key[0]
    answer += (now_group_key[0] ** 2)
    for element in group_list[now_group_key]:
        x, y, _ = element
        block_map[x][y] = -2
    group_list.pop(now_group_key)

    gravity()
    rotate()
    gravity()

print(answer)