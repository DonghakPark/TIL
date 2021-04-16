"""
투에-모스 문자열 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""


def recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2:
        return 1 - recursive(n//2)
    else:
        return recursive(n//2)

k = int(input())

print(recursive(k-1))
