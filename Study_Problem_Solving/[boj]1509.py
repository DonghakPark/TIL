"""
팰린드롬 분할 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""

import sys

A = sys.stdin.readline().strip()
N = len(A)

dp = [[0 for i in range(N+1)]for j in range(N+1)]
result = [sys.maxsize] * (N+1)
result[0] = 0

for i in range(1, N+1):
    dp[i][i] = 1

for i in range(1, N):
    if A[i-1] == A[i]:
        dp[i][i+1] = 1

for i in range(2,N):
    for j in range(1, N + 1 - i):
        if A[j-1] == A[j+i-1] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1

for i in range(1, N+1):
    result[i] = min(result[i], result[i-1] + 1)

    for j in range(i+1, N+1):
        if dp[i][j] != 0:
            result[j] = min(result[j], result[i-1] + 1)

print(result[N])