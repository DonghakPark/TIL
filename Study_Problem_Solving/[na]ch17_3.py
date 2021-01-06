"""
화성 탐사 문제
author : donghak park
contact : donghark03@naver.com
"""
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

T = int(input())
for test_case in range(T):
    N = int(input())

    cost = []
    for _ in range(N):
        cost.append(list(map(int, input().split())))

    distance = [[INF] * N for _ in range(N)]

    x,y = 0, 0

    q = [(cost[x][y], x, y)]
    distance[x][y] = cost[x][y]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            c = dist + cost[nx][ny]

            if c < distance[nx][ny]:
                distance[nx][ny] = c
                heapq.heappush(q, (c,nx,ny))
    print(distance[N-1][N-1])