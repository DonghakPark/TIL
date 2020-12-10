T = int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    global visited
    global Arr
    global answer

    Q = []
    Q.append([x,y])

    while Q:
        x1, y1 = Q.pop(0)
        visited[y1][x1] = True

        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]

            if nx < M and nx >= 0 and ny < N and ny >=0 and visited[ny][nx] is False:
                if [nx,ny] in Arr:
                    visited[ny][nx] = True
                    Q.append([nx,ny])
    answer += 1
    return True


for tc in range(T):

    M, N, K = map(int, input().split())

    Arr = []
    for i in range(K):
        Arr.append(list(map(int, input().split())))

    visited = [ [False for _ in range(M)] for _ in range(N) ]
    answer = 0

    for a in range(M):
        for b in range(N):

            if [a,b] in Arr:
                if visited[b][a] is not True:
                    bfs(a,b)
    print(answer)