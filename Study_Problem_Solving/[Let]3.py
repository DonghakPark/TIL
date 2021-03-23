#sol

from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def find_section(x,y):
    global visited
    global answer

    Q = deque()
    Q.append([x,y])
    value = Arr[x][y]
    visited[x][y] = True

    while Q:
        X,Y = Q.popleft()

        for i in range(4):
            nx, ny = X + dx[i], Y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == False and Arr[nx][ny] == value:
                    Q.append([nx, ny])
                    visited[nx][ny] = True


N = int(input())
Arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

answer = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            find_section(i, j)
            answer += 1

print(answer)
