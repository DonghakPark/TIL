"""
여행 계획 문제
author : donghak park
contact : donghark03@naver.com
"""
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N,M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


parent = [0] * (N+1)

for i in range(1, N+1):
    parent[i] = i

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            union_parent(parent, i+1, j+1)

flag = True
rou = list(map(int, input().split()))

check = find_parent(parent, rou[0])
for i in range(1,len(rou)):
    if find_parent(parent, rou[i]) != check:
        flag = False
        print("NO")
        break

if flag == True:
    print("YES")
