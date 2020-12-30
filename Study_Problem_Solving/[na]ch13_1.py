"""
특정 거리의 도시 찾기
author : donghak park
contact : donghark03@naver.com
"""
from collections import deque

N, M, K, X = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = (map(int, input().split()))
    arr[a].append(b)

Q = deque([X])
min_dist = [-1] * (N+1)
min_dist[X] = 0
while Q:
    now = Q.popleft()

    for next_node in arr[now]:
        if min_dist[next_node] == -1:
            min_dist[next_node] = min_dist[now] + 1
            Q.append(next_node)

check = False
for i in range(1, N+1):
    if min_dist[i] == K:
        print(i)
        check = True

if check == False:
    print(-1)