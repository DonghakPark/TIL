"""
인구 이동 문제
author : donghak park
contact : donghark03@naver.com
"""
import math
from collections import deque

N, L, R = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))
answer = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def deter(a,b,num):
    global perm

    united = []
    united.append((a,b))

    Q = deque([])
    Q.append([a,b])
    perm[a][b] = num
    summary = arr[a][b]
    count = 1
    while Q:
        x, y = Q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx < N and ny < N:
                diff = abs(arr[x][y] - arr[nx][ny])
                if diff <= R and diff >= L and perm[nx][ny] == -1:
                    perm[nx][ny] = num
                    Q.append([nx, ny])
                    summary += arr[nx][ny]
                    count += 1
                    united.append((nx,ny))
    for i,j in united:
        arr[i][j] = summary//count
    return count

while True:
    num = 0
    perm = [[-1] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if perm[i][j] == -1 :

                deter(i,j,num)
                num += 1
    answer += 1

    if num == (N*N):
        break

print(answer-1)
