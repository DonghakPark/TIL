"""
장난감조립 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""
from collections import defaultdict,deque

N = int(input())

degree = [0] * (N + 1)
graph = [[] for _ in range(N+1)]

M = int(input())

for _ in range(M):
    x, y, k = map(int, input().split())
    degree[x] += 1
    graph[y].append([x,k])

Q = deque()
need = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    if degree[i] == 0:
        Q.append(i)
        need[i][i] = 1

while Q:
    now = Q.popleft()
    for element in graph[now]:
        for i in range(1,N+1):
            need[element[0]][i] += element[1] * need[now][i]
        degree[element[0]] -= 1
        if degree[element[0]] == 0:
            Q.append(element[0])
for i in range(len(need[0])):
    if need[N][i] != 0:
        print("{} {}".format(i, need[N][i]))