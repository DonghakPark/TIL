"""
토마토 문제 - 2
author : donghak park
contact : donghark03@naver.com
"""
from collections import deque

def BFS():
    while Q:
        x,y,z = Q.popleft()

        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
                if arr[nx][ny][nz] == 0:
                    arr[nx][ny][nz] = arr[x][y][z] + 1
                    Q.append((nx,ny,nz))


M, N, H = map(int, input().split())
arr = [[] for _ in range(H)]
for i in range(H):
    for _ in range(N):
        arr[i].append(list(map(int, input().split())))

dx = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
dz = [1,-1,0,0,0,0]

answer = 0
Q = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                Q.append((i,j,k))

BFS()
Flag = False

for i in range(H):
    for j in range(N):
        for k in range(M):

            if arr[i][j][k] == 0:
                Flag = True
                break
            answer = max(answer, arr[i][j][k])

if Flag:
    answer = -1
elif answer == -1:
    answer = 0
else:
    answer -= 1

print(answer)