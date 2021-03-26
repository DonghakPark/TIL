"""
키 순서 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""
from collections import defaultdict, deque

N, M = map(int, input().split())

order_h = defaultdict(list)
order_l = defaultdict(list)
degree = [0] * (N+1)
for _ in range(M):
    Low, High = map(int, input().split())
    order_h[Low].append(High)
    order_l[High].append(Low)


for key in order_h.keys():
    visited = [0] * (N+1)
    Q = deque()
    Q.append(key)
    visited[key] = 1

    while Q:
        now = Q.popleft()
        if now not in order_h.keys():
            continue
        for element in order_h[now]:
            if visited[element] == 0:
                visited[element] = 1
                degree[element] += 1
                Q.append(element)

for key in order_l.keys():
    visited = [0] * (N+1)
    Q = deque()
    Q.append(key)
    visited[key] = 1

    while Q:
        now = Q.popleft()
        if now not in order_l.keys():
            continue
        for element in order_l[now]:
            if visited[element] == 0:
                visited[element] = 1
                degree[element] += 1
                Q.append(element)

print(degree.count(N-1))