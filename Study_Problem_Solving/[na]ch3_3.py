N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

MAX = 0

for element in arr:
    element.sort()
    MAX = max(MAX, element[0])

print(MAX)