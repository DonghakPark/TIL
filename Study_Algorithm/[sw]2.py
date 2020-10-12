# 내가 푼 풀이

#Dynamic Programming

T = int(input())

for test_case in range(1, T+1):
    d,m,m_3,y = map(int, input().split())
    a = list(map(int,input().split()))
    dp = [0] * 15
    min_value = 1e9

    for i in range(11, -1, -1):
        #일로 계산시
        dp[i] = min(dp[i+1]+a[i]*d, dp[i+1] + m, dp[i+3] + m_3, y)
    print("#{} {}".format(test_case, dp[0]))



#Recursive

