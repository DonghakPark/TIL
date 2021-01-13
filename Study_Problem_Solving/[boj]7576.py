"""
토마토 문제 - 1
author : donghak park
contact : donghark03@naver.com
"""
from collections import deque
import sys
input = sys.stdin.readline


def BFS():
    while Q:
        x,y = Q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] +1
                    Q.append((nx,ny))

N, M = map(int, input().split())
arr = []

for _ in range(M):
    arr.append(list(map(int, input().split())))

dx = [0,0,-1,1]
dy = [1,-1,0,0]
Q = deque()

for i in range(M):
    for j in range(N):
        if arr[i][j] == 1:
            Q.append((i,j))

BFS()

answer = 0
flag = False

for i in range(M):
    for j in range(N):

        if arr[i][j] == 0:
            flag = True
            break
        answer = max(answer, arr[i][j])

if flag:
    print(-1)
elif answer == -1:
    print(0)
else:
    print(answer-1)