"""
특정한 최단 경로 문제
author : donghak park
contact: donghark03@naver.com
"""

import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start_node, end):
    distance = [INF] * (N + 1)

    Q = []
    heapq.heappush(Q, (0, start_node))
    distance[start_node] = 0

    while Q:
        now_dist, now_node = heapq.heappop(Q)

        for next_dist, next_node in graph[now_node]:
            next_dist = next_dist + now_dist

            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heapq.heappush(Q, [next_dist, next_node])

    return distance[end]


N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    start, end, cost = map(int, input().split())

    graph[start].append([cost,end])
    graph[end].append([cost,start])

must1, must2 = map(int, input().split())

temp1 = dijkstra(1, must1) + dijkstra(must1, must2) + dijkstra(must2, N)
temp2 = dijkstra(1, must2) + dijkstra(must2, must1) + dijkstra(must1, N)

if temp1 >= INF and temp2 >= INF:
    print(-1)
else:
    print(min(temp1, temp2))
