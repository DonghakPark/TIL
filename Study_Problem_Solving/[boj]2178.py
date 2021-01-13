"""
미로 탐색 문제
author : donghak park
contact : donghark03@naver.com
"""
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
dist = [[0] * M for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

Q = deque()
Q.append((0,0))
dist[0][0] = 1
visited[0][0] = True

while Q:
    x,y = Q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < N and ny < M:
            if visited[nx][ny] is False and arr[nx][ny] == 1:
                dist[nx][ny] = dist[x][y] + 1
                Q.append((nx, ny))
                visited[nx][ny] = True

print(dist[N-1][M-1])