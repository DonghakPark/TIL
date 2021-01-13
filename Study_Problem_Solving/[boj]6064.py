"""
카잉 달력 문제
author : donghak park
contact : donghark03@naver.com
"""

T = int(input())
for test_case in range(T):
    M,N,x,y = map(int, input().split())
    answer = -1
    x = x-1
    y = y-1
    for i in range(x, (N*M)+1, M):
        if (i)%N == y:
            answer = i + 1
            break
    print(answer)
