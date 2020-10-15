#등산로 조성 문제

def dfs(y,x,cnt,k,n):
    global res
    if (res < cnt + 1):
        res = cnt + 1
    visited[y][x] = 1
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ( ny >=0 and ny <n and nx >= 0 and nx <n):
            if(visited[ny][nx] == 0):
                if(arr[ny][nx] < arr[y][x]):
                    dfs(ny,nx,cnt+1,k,n)
                elif(arr[ny][nx] - k < arr[y][x]):
                    pre = arr[ny][nx]

                    arr[ny][nx] = arr[y][x] - 1
                    dfs(ny,nx,cnt+1,0,n)

                    arr[ny][nx] = pre
    visited[y][x] = 0

T = int(input())

for test_case in range(1, T+1):
    n, k = map(int, input().split())

    arr = []

    for i in range(n):
        arr.append(list(map(int, input().split())))

    res = 0
    maxV = 0
    visited = [ [0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
                if (maxV < arr[i][j]):
                    maxV = max(maxV, arr[i][j])
    v = []
    for i in range(n):
        for j in range(n):
                if(arr[i][j] == maxV):
                    v.append([i,j])
    for i in range(len(v)):
        dfs(v[i][0], v[i][1], 0, k, n)
    print("#{} {}".format(test_case, res))