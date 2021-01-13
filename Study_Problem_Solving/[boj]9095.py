"""
1,2,3 더하기 문제
author : donghak park
contact : donghark03@naver.com
"""

T = int(input())
for test_case in range(T):
    N = int(input())
    dp = [0] * (11)

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    if N > 3:
        for i in range(4, N+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[N])