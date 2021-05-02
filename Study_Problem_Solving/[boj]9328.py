"""
열쇠 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""

T = int(input())

for _ in range(T):
    h, w = map(int, input().split())
    arr = []
    for _ in range(h):
        arr.append(list(input()))

    already = list(input())

    # TODO : 나중에 풀어볼 것것