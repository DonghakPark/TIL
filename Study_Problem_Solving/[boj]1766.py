"""
Author : Donghak Park
BOJ 1766
"""

from collections import defaultdict
import heapq

N, M = map(int, input().split())


degree = [0 for _ in range(N+1)]
problem = [[] for i in range(N +1)]
heap = []
answer = []

for i in range(M):
    pre, post = map(int, input().split())
    problem[pre].append(post)
    degree[post] += 1

for i in range(1, N+1):
    if degree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    now = heapq.heappop(heap)
    answer.append(now)

    for j in problem[now]:
        degree[j] -= 1
        if degree[j] == 0:
            heapq.heappush(heap, j)

for i in answer:
    print(i, end = " ")