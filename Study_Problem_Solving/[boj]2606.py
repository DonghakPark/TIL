"""
바이러스 문제
author : donghak park
contact : donghark03@naver.com
"""


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(M)]

parent = [0] * (N+1)

for i in range(1, N+1):
    parent[i] = i

for i in range(2):
    for x,y in arr:
        union(parent,x,y)

answer = 0
for i in range(2,len(parent)):
    if parent[i] == 1:
        answer += 1
print(answer)