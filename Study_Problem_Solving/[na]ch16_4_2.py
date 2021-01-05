"""
가장 긴 증가하는 부분 순열
author : donghak park
contact : donghark03@naver.com
"""

N = int(input())
arr = list(map(int, input().split()))

result = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            result[i] = max(result[i], result[j] +1)

print(max(result))