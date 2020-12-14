# 퇴사 문제

N = int(input())

T = []
P = []

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N+1)
max_value = 0

for i in range(N-1, -1, -1):
    time = i + T[i]

    if time <= N:
        dp[i] = max(dp[time]+P[i], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
print(max_value)



