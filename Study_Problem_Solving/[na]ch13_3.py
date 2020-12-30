"""
경쟁적 전염 문제
author : donghak park
contact : donghark03@naver.com
"""
N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

S, X, Y = map(int, input().split())

time = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

Q = []

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            Q.append([arr[i][j],i,j])
Q.sort(key = lambda x:(x[0]))

while time < S:
    count = 0
    k = len(Q)
    while k > count:

        num, x, y = Q.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >=0 and ny >=0 and ny < N and nx < N:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = num
                    Q.append([arr[nx][ny],nx,ny])
        count += 1

    Q.sort(key = lambda x:(x[0]))
    time += 1

print(arr[X-1][Y-1])