"""
미로 탐색 문제
author : donghak park
contact : donghark03@naver.com
"""
from collections import deque

N, M = map(int, input().split())
arr = []
for _ in range(N):
    temp = list(input())
    arr.append(list(map(int, temp)))

visited = [[False] * M for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

Q = deque([])
Q.append([0,0])

while Q:
    x,y = Q.popleft()
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < N and ny < M:
            if visited[nx][ny] is False and arr[nx][ny] != 0:
                arr[nx][ny] = arr[x][y] + 1
                Q.append([nx, ny])
print(arr[N-1][M-1])