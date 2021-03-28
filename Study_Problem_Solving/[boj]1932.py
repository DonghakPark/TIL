"""
정수 삼각형 문제
author : donghak park
contact : donghark03@naver.com
"""
N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

visited = []
for f in range(1,N+1):
    temp = [0] * f
    visited.append(temp)

visited[0][0] = arr[0][0]

for i in range(1,N):
    for j in range(len(arr[i])):
        left = 0
        right = 0

        if j-1 >= 0:
            left = visited[i-1][j-1]

        if j <= len(visited[i-1])-1:
            right = visited[i-1][j]

        visited[i][j] = max((arr[i][j] + left), (arr[i][j] + right))

print(max(visited[N-1]))