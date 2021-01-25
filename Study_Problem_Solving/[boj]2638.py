"""
치즈 문제
author : donghak park
contact: donghark03@naver.com
"""

import sys
from collections import deque

input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def make_air(i,j):
    visited = [[0] * M for _ in range(N)]
    Q = deque()
    Q.append([i,j])
    visited[i][j] = 1

    while Q:
        x, y = Q.popleft()

        for k in range(4):

            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] != 1 and visited[nx][ny] == 0:
                    arr[nx][ny] = 2
                    Q.append([nx,ny])
                    visited[nx][ny] = 1


def check(i,j):
    x, y, = i, j
    count = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 2:
                count += 1
    if count >= 2:
        return True
    else:
        return False

def is_end():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                return False
    return True

N, M = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

make_air(0,0)

time = 0
while True:

    time += 1
    update_list = []

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                if check(i,j):
                    update_list.append([i,j])

    for i,j in update_list:
        arr[i][j] = 0

    make_air(0,0)

    if is_end():
        break

print(time)