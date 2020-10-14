# 테트로미노

N,M = map(int, input().split())

answer = 0

Arr = []

for _ in range(N):
    Arr.append(list(map(int, input().split())))

visited = [[0]*M for _ in range(N)]


stack_Arr = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y,sum,depth):

    global answer
    global visited

    sum += Arr[x][y]

    if depth == 1:
        if answer < sum:
            answer = sum
            return
        else:
            return

    stack_Arr.append([x,y])
    visited[x][y] = 1

    for x_1, y_1 in stack_Arr:

        for i in range(4):
            nx = x_1 + dx[i]
            ny = y_1 + dy[i]

            if nx >=0 and ny >= 0 and nx < N and ny < M:
                if visited[nx][ny] == 0:
                    dfs(nx, ny, sum, depth-1)


    visited[x][y] = 0
    stack_Arr.pop()

    return


for i in range(N):
    for j in range(M):
        dfs(i,j,0,4)

print(answer)


