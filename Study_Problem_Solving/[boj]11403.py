"""
경로 찾기 문제
author : donghak park
contact: donghark03@naver.com
"""
import sys
input = sys.stdin.readline

N = int(input())
visited = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for a in range(N):
        for b in range(N):
            visited[a][b] = max(visited[a][b], visited[a][k]&visited[k][b])

for i in range(N):
    for j in range(N):
        print(visited[i][j], end=" ")
    print()

