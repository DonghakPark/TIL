"""
LCS 문제
author : donghak park
contact: donghark03@naver.com
TODO : 나중에 다시 풀어보기
"""

S1 = list(input())
S2 = list(input())

S1_length = len(S1)
S2_length = len(S2)

dp = [[0] * (S2_length + 1) for _ in range(S1_length +1)]

for i in range(S1_length):
    for j in range(S2_length):
        if S1[i] == S2[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(dp[S1_length][S2_length])


