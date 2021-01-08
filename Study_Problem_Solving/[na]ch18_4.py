"""
행성 터널 문제
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


N = int(input())

parent = [0] * (N + 1)

result = 0
route = []

for i in range(1, N + 1):
    parent[i] = i

arr1 = []
arr2 = []
arr3 = []

for i in range(1, N+1):
    x, y, z = map(int, input().split())
    arr1.append((x,i))
    arr2.append((y,i))
    arr3.append((z,i))

arr1.sort()
arr2.sort()
arr3.sort()

for i in range(N-1):
    route.append((abs(arr1[i+1][0] - arr1[i][0]), arr1[i][1], arr1[i+1][1]))
    route.append((abs(arr2[i+1][0] - arr2[i][0]), arr2[i][1], arr2[i+1][1]))
    route.append((abs(arr3[i+1][0] - arr3[i][0]), arr3[i][1], arr3[i+1][1]))

route.sort()

for edge in route:
    cost, x, y = edge

    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost

print(result)

