"""
병사 배치하기 문제
author : donghak park
contact : donghark03@naver.com
"""

N = int(input())
arr = list(map(int, input().split()))

result = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[i] < arr[j]:
            result[i] = max(result[j] + 1, result[i])

print(N - max(result))
