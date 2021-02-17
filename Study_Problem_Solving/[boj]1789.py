"""
수들의 합
author : donghak park
contact: donghark03@naver.com
"""

S = int(input())

answer = 0
start = 1
end = S

while start <= end:
    mid = (start + end)//2
    sum_mid = mid * (mid + 1) // 2

    if sum_mid <= S:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
