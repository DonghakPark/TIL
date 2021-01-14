"""
적록색약 문제
author : donghak park
contact: donghark03@naver.com
"""
from collections import deque

def normal(a, b, Arr):

    Q = deque()
    Q.append([a,b])
    visited_n[a][b] = 1

    while Q:
        x,y = Q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited_n[nx][ny] == 0 and Arr[x][y] == Arr[nx][ny]:
                    Q.append([nx,ny])
                    visited_n[nx][ny] = normal

N = int(input())
arr = [list(input()) for _ in range(N)]
arr2 = [["A"] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == "R":
            arr2[i][j] = "G"
        else:
            arr2[i][j] = arr[i][j]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

normal_n = 0
visited_n = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited_n[i][j] == 0:
            normal_n += 1
            normal(i,j,arr)

print(normal_n , end=" ")

normal_n = 0
visited_n = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited_n[i][j] == 0:
            normal_n += 1
            normal(i,j,arr2)

print(normal_n)
