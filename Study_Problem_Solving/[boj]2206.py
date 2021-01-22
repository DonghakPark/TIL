"""
벽 부수고 이동하기 문제
author : donghak park
contact: donghark03@naver.com
"""

import sys
from collections import deque
input = sys.stdin.readline

def BFS():
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

    Q = deque()
    Q.append([0,0,1])
    visited[0][0][1] = 1

    while Q:
        x, y, possible = Q.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][possible]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1 and possible == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    Q.append([nx, ny, 0])
                elif visited[nx][ny][possible] == 0 and arr[nx][ny] == 0:
                    Q.append([nx,ny,possible])
                    visited[nx][ny][possible] = visited[x][y][possible] + 1

    return -1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, list(input().rstrip()))))

print(BFS())