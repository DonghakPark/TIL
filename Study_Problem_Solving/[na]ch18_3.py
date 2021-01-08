"""
어두운 길 문제
author : donghak park
contact : donghark03@naver.com
"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N,M = map(int, input().split())

parent = [0] * (N+1)

for i in range(1, N+1):
    parent[i] = i

road = []
ori_cost = 0
result = 0

for _ in range(M):
    x,y,z = map(int, input().split())
    road.append([z,x,y])
    ori_cost += z

road.sort()

for edge in road:
    cost, x, y = edge

    if find_parent(parent,x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost

print(ori_cost - result)
