"""
파도반 수열
author : donghak park
contact: donghark03@naver.com
"""

T = int(input())

for test_case in range(T):
    N = int(input())
    P = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    answer = 0
    if N <= 10:
        answer = P[N]
    else:
        i = 11
        while i <= N:
            P.append( P[i-2] + P[i-3] )
            i += 1

        answer = P[N]

    print(answer)