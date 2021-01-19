"""
최단 경로 문제
author : donghak park
contact: donghark03@naver.com
"""
import sys, heapq
INF = sys.maxsize
input = sys.stdin.readline


def dijstra(start):

    distance = [INF] * (V+1)
    Q = []

    heapq.heappush(Q, [0, start])
    distance[start] = 0

    while Q:
        now_cost, now_vertex = heapq.heappop(Q)


        for next_cost, next_vertex in graph[now_vertex]:
            next_cost = next_cost + now_cost
            if next_cost < distance[next_vertex]:
                distance[next_vertex] = next_cost
                heapq.heappush(Q, [next_cost, next_vertex])

    return distance

V, E = map(int, input().split())

K = int(input()) # 시작 정점

graph = [[] for _ in range(V+1)]

for _ in range(E):
    start, end, cost = map(int, input().split())
    graph[start].append([cost, end])

answer_arr = dijstra(K)

for i in range(1, len(answer_arr)):
    if i == K:
        print(0)
    elif answer_arr[i] == INF:
        print("INF")
    else:
        print(answer_arr[i])