"""
연구소 3문제
Author : DongHak Park
"""
import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

input = sys.stdin.readline
answer = int(1e9)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def check_map(now_map):
    global N

    for i in range(N):
        for j in range(N):
            if now_map[i][j] == 0:
                return False
    return True


def move_virus(virus_arr, new_map):
    global answer
    global N
    visited = [[0] * N for _ in range(N)]

    new_map = deepcopy(new_map)

    new_virus = deque()
    new_virus.extend(virus_arr)
    max_cnt = 0
    while new_virus:
        x, y, now_time = new_virus.popleft()
        visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and new_map[nx][ny] != 1:
                visited[nx][ny] = 1
                if new_map[nx][ny] == 0:
                    new_map[nx][ny] = 2
                    max_cnt = now_time + 1
                new_virus.append([nx, ny, now_time + 1])

    if check_map(new_map):
        answer = min(answer, max_cnt)



# 0은 빈칸, 1은 벽, 2는 바이러스 위치
N, M = map(int, input().split())
virus_map = []
for _ in range(N):
    virus_map.append(list(map(int, input().split())))

virus_loc = []
for i in range(N):
    for j in range(N):
        if virus_map[i][j] == 2:
            virus_loc.append([i, j, 0])

candidate = list(combinations(virus_loc, M))

for element in candidate:
    move_virus(element, virus_map)

if answer == int(1e9):
    print(-1)
else:
    print(answer)
