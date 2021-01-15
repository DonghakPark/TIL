"""
ATM 문제
author : donghak park
contact: donghark03@naver.com
"""

N = int(input())
P = list(map(int, input().split()))

P.sort()

answer = 0
for i in range(1, N+1):
    answer += sum(P[:i])

print(answer)
