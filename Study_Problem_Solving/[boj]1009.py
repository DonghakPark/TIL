"""
분산처리 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""

T = int(input())
for test_case in range(T):
    a, b = map(int, input().split())

    answer = 0
    if a % 10 == 0:
        answer = 10
    else:
        it = 4 + (b % 4)
        ret = str(a ** it)
        answer = ret[-1]

    print(answer)
