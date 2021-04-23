"""
점프와 순간 이동 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""


def solution(n):
    ans = 0
    ans += 1
    now = n
    while True:

        if now == 1:
            break

        if now % 2 == 0:
            now = now // 2
        else:
            now -= 1
            ans += 1

    return ans
