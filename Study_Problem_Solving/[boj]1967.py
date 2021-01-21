"""
트리의 지름 문제
author : donghak park
contact: donghark03@naver.com
"""
import sys, heapq
INF = sys.maxsize
input = sys.stdin.readline

def dijstra(start):
    distance = [INF] * (N+1)
    Q = []

    heapq.heappush(Q, [0, start])
    distance[start] = 0

    while Q:
        now_cost, now_vertex = heapq.heappop(Q)

        for next_cost, next_vertex in graph[now_vertex]:
            if next_cost + now_cost < distance[next_vertex]:
                next_cost += now_cost
                distance[next_vertex] = next_cost
                heapq.heappush(Q, [next_cost, next_vertex])

    return distance

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    start, end, cost = map(int, input().split())
    graph[start].append([cost, end])
    graph[end].append([cost, start])

temp = dijstra(1)[1:]
new_start = temp.index(max(temp))+1
answer = dijstra(new_start)[1:]
print(max(answer))
