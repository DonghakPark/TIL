"""
정확한 순위 문제
author : donghak park
contact : donghark03@naver.com
"""

N, M = map(int, input().split())

arr = [[1e9] * N for _ in range(N)]

for i in range(N):
    arr[i][i] = 1

for _ in range(M):
    x,y = map(int, input().split())
    arr[x-1][y-1] = 1

for k in range(N):
    for a in range(N):
        for b in range(N):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

answer = 0
for i in range(N):
    count = 0
    for j in range(N):
        if arr[i][j] != 1e9 or arr[j][i] != 1e9:
            count +=1
    if count == N:
        answer += 1

print(arr)


