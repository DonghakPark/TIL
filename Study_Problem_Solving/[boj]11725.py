"""
트리의 부모 찾기 문제
author : donghak park
contact: donghark03@naver.com
"""
import sys
input = sys.stdin.readline

N = int(input())
parent = [0] * (N+1)
visited = [0] * (N+1)
tree = {}

for _ in range(N-1):
    x, y = map(int, input().split())

    if x in tree.keys():
        tree[x].append(y)
    else:
        tree[x] = [y]

    if y in tree.keys():
        tree[y].append(x)
    else:
        tree[y] = [x]
Q = []
for element in tree[1]:
    Q.append([element, 1])

while Q:
    node, par = Q.pop(0)

    parent[node] = par
    visited[node] = 1

    for element in tree[node]:
        if visited[element] == 0:
            Q.append([element, node])

for i in range(2, len(parent)):
    print(parent[i])