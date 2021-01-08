"""
탑승구 문제
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

G = int(input())
P = int(input())

parent = [0] * (G+1)

for i in range(1, G+1):
    parent[i] = i
result = 0
for _ in range(P):
    data = find_parent(parent, int(input()))
    if data == 0:
        break
    union_parent(parent, data, data -1)
    result += 1

print(result)