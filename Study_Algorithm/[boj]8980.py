import sys
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())
arr = []

for i in range(M):
    temp = list(map(int, input().split()))
    arr.append(temp)

arr.sort(key = lambda x :(x[1],x[0],-x[2]))

Answer = [0] * (N+1)
result = 0

for element in arr:
    min_c = 2e9
    for i in range(element[0], element[1]):
        min_c = min( (C - Answer[i]), min_c, element[2])

    for i in range(element[0], element[1]):
        Answer[i] += min_c
    result += min_c

print(result)