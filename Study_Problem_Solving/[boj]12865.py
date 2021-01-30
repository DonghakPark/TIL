"""
평범한 배낭 문제
author : donghak park
contact: donghark03@naver.com
TODO : 다시 한번 풀어볼 것 (Gold 5)
"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.insert(0, [0,0])

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        Weight, Value = arr[i]

        if j < Weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(Value + dp[i-1][j-Weight], dp[i-1][j])

answer = dp[N][K]

print(answer)