#인구 이동
import math
from collections import deque

N, L, R = map(int, input().split())

ori = []
temp = [[0]* N for _ in range(N)]

for _ in range(N):
    ori.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
color = 0
#########################

def coloring(x, y):
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >=0 and nx < N and ny >= 0 and ny < N:
                diff = abs( ori[x][y] - ori[nx][ny] )
                if diff >= L and diff <= R and temp[nx][ny] == 0:
                    temp[nx][ny] = color
                    q.append((nx,ny))
                    # coloring(nx, ny)

def get_population():
    arr = []
    arr.append(0)

    for col in range(1,color+1):
        count = 0
        sum = 0
        for i in range(N):
            for j in range(N):
                if temp[i][j] == col:
                    sum += ori[i][j]
                    count += 1

        arr.append(math.floor(sum/count))

    for col in range(1, color+1):
        for i in range(N):
            for j in range(N):
                if temp[i][j] == col:
                    ori[i][j] = arr[col]

while True:

    for i in range(N):
        for j in range(N):

            if temp[i][j] == 0:
                color += 1
                temp[i][j] = color
                coloring(i,j)

    #색칠 끝남

    get_population()

    if color == N*N:
        break

    temp = [[0] * N for _ in range(N)]
    color = 0
    answer += 1

print(answer)