"""
빙산 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""
import sys, copy
from collections import deque
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def check_answer():
    visited = [[0] * M for _ in range(N)]
    Q = deque()
    count = 1
    for i in range(N):
        for j in range(M):
            if count == 3:
                return True

            if ice[i][j] != 0 and visited[i][j] == 0:
                Q.append([i,j])
                visited[i][j] = count
                while Q:
                    x, y = Q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < N and 0 <= ny < M:
                            if visited[nx][ny] == 0 and ice[nx][ny] != 0:
                                visited[nx][ny] = count
                                Q.append([nx,ny])
                count += 1

    return False

N, M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]
time = 0
answer = 0
while True:

    if check_answer():
        answer = time
        break
    if ice.count([0]*M) == N:
        break

    temp = copy.deepcopy(ice)
    for i in range(N):
        for j in range(M):
            if temp[i][j] != 0:
                count = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < N and 0 <= ny <M:
                        if ice[nx][ny] == 0:
                            count += 1
                temp[i][j] -= count
                if temp[i][j] < 0:
                    temp[i][j] = 0

    ice = copy.deepcopy(temp)
    time += 1

print(answer)
