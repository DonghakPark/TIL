# 등산로 조성 문제

T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x, y, N, K, high_int):
    now_x = x
    now_y = y

    length = 0

    for i in range(4):
        nx = now_x + dx[]
        ny = now_y + dy[]

        if 0 <= nx and nx < N and 0 <= ny and ny < N:
            if arr[nx][ny] < high_int:
                dfs(nx,ny,N,K,arr[nx][ny])

            for k in range(1,K+1):
                if arr[nx][ny]-k < high_int:
                    dfs(nx,ny,N,K-k, arr[nx][ny])
                    length +=1

for test_case in range(1, T+1):

    N, K = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    ## 입력 완료

    high = []
    high_int = 0

    for element in arr:
        for i in element:
            if i >= high_int:
                high_int = i

    for i in range(N):
        for j in range(N):
            if arr[i][j] == high_int:
                high.append([i,j])
    result = 0

    for x,y in high:
        temp = dfs(x,y,N,K,0,high_int)
        if temp >= result:
            result = temp

    print("#{} {}".format(test_case, result))



