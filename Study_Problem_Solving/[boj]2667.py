"""
단지 번호 붙이기 문제
author : donghak park
contact : donghark03@naver.com
"""
from collections import deque


def BFS(a, b, count):
    global visited

    Q = deque()
    Q.append((a, b))
    visited[a][b] = count

    while Q:
        x, y = Q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and arr[nx][ny] == 1:
                    Q.append((nx, ny))
                    visited[nx][ny] = count


N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
count = 1
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(N):
    for j in range(N):

        if arr[i][j] == 1 and visited[i][j] == 0:
            BFS(i,j,count)
            count += 1

sum = 0
answer = []
for i in range(1, count):
    for a in range(N):
        for b in range(N):
            if visited[a][b] == i:
                sum += 1
    answer.append(sum)
    sum = 0

answer.sort()
print(count-1)
for element in answer:
    print(element)