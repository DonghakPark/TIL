"""
트리의 지름 문제
author : donghak park
contact: donghark03@naver.com
"""
import sys
from collections import deque

input = sys.stdin.readline

def BFS(i):
    Q = deque()
    Q.append([0,i])

    max_vertex = 0
    max_dist = 0

    visited.add(i)

    while Q:

        now_dist, now_vertex = Q.popleft()

        if now_dist > max_dist:
            max_dist = now_dist
            max_vertex = now_vertex

        for element in graph[now_vertex]:
            next_vertex, next_dist = element

            if next_vertex not in visited:
                Q.append([now_dist+next_dist, next_vertex])
                visited.add(next_vertex)

    return max_dist, max_vertex

V = int(input())
graph = {}

for i in range(V):
    temp = list(map(int, input().split()))[:-1]
    index = temp.pop(0)
    graph[index] = []
    while temp:
        j = temp.pop(0)
        value = temp.pop(0)

        graph[index].append([j,value])

visited = set()
a,b = BFS(1)
visited.clear()
answer, _ = BFS(b)
print(answer)

