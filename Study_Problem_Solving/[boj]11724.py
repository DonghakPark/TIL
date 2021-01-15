"""
연결 요소의 개수 문제
author : donghak park
contact: donghark03@naver.com
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

N, M = map(int, input().split())
parent = [0] * (N+1)

for i in range(1, N+1):
    parent[i] = i

for _ in range(M):
    start, end = map(int, input().split())
    union(parent,start,end)

for i in range(1,N+1):
    find_parent(parent,i)

answer = set(parent)
print(len(answer)-1)