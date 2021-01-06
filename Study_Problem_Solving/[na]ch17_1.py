"""
플로이드 문제
author : donghak park
contact : donghark03@naver.com
"""

N = int(input())
M = int(input())
arr = [[int(1e9)] * N for _ in range(N)]
for i in range(N):
    arr[i][i] = 0

for _ in range(M):
    x,y,v = map(int, input().split())

    if arr[x-1][y-1] == 1e9:
        arr[x-1][y-1] = v
    elif arr[x-1][y-1] > v:
        arr[x-1][y-1] = v

for k in range(N):
    for a in range(N):
        for b in range(N):
            arr[a][b] = min(arr[a][b], (arr[a][k] + arr[k][b]))

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1e9:
            print(0, end = " ")
        else:
            print(arr[i][j], end = " ")
    print()
