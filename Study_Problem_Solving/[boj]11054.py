"""
가장 긴 바이토닉 부분 수열 문제
author : donghak park
contact : donghark03@naver.com
"""

N = int(input())
arr = list(map(int, input().split()))

result = [1] * N
result2 = [1] * N
answer = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            result[i] = max(result[i], result[j] + 1 )
for i in range(N-1, -1, -1):
    for j in range(i+1, N):
        if arr[i] > arr[j]:
            result2[i] = max(result2[i], result2[j] + 1)
    answer[i] = result2[i] + result[i] - 1

print(max(answer))