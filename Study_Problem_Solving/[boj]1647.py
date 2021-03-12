"""
도시 분할 계획 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def make_union(parent, a, b):
    a = parent[a]
    b = parent[b]
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
answer = 0

Q = []
parent = [0] * (N + 1)
for i in range(1, N+1):
    parent[i] = i

for _ in range(M):
    a, b, c = map(int, input().split())
    Q.append([c,a,b])

Q.sort()
last = 0

for element in Q:
    cost, start, end = element
    if find_parent(parent, start) != find_parent(parent, end):
        make_union(parent, start, end)
        answer += cost
        last = cost

print(answer - last)