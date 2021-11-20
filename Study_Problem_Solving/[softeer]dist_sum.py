import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

def solution(i):
    dist = [int(1e9)] * (N+1)

    Q = []
    heapq.heappush(Q, [0, i])
    dist[i] = 0

    while Q:
        now_cost, now_vertex = heapq.heappop(Q)

        if dist[now_vertex] < now_cost:
            continue

        for next_cost, next_vertex in graph[now_vertex]:
            if next_cost + now_cost < dist[next_vertex]:
                dist[next_vertex] = next_cost + now_cost
                heapq.heappush(Q, [next_cost + now_cost, next_vertex])
    print(sum(dist[1:]))

N = int(input())

graph = defaultdict(list)

for _ in range(N - 1):
    start, end, cost = map(int, input().split())
    graph[start].append([cost, end])
    graph[end].append([cost, start])

for i in range(1, N+1):
    solution(i)