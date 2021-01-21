"""
최소비용 구하기 문제
author : donghak park
contact: donghark03@naver.com
"""
import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijstra(start):
    distance = [INF] * (N+1)

    Q = []
    heapq.heappush(Q, [0, start])
    distance[start] = 0

    while Q:
        now_cost, now_vertex = heapq.heappop(Q)

        for next_cost, next_vertex in graph[now_vertex]:
            if distance[next_vertex] > next_cost + now_cost:
                next_cost += now_cost
                heapq.heappush(Q, [next_cost, next_vertex])
                distance[next_vertex] = next_cost

    return distance


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append([cost, end])

A, B = map(int, input().split())
answer = dijstra(A)

print(answer[B])
