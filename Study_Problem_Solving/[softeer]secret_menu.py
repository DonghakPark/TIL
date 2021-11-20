import sys

N, M, K = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

dp_table = [[0] * (len(arr2) + 2) for _ in range(len(arr1) + 2)]
answer = 0
for i in range(len(arr1)):
    for j in range(len(arr2)):
        print(i,j)
        if arr1[i] == arr2[j]:
            dp_table[i+1][j+1] = dp_table[i][j] + 1
            answer = max(answer, dp_table[i+1][j+1])

print(answer)