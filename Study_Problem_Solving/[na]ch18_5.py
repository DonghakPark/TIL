"""
최종 순위 문제
author : donghak park
contact : donghark03@naver.com
"""

TC = int(input())

for test_case in range(TC):
    N = int(input())

    last = []
    for _ in range(N):
        last.append(list(map(int, input().split())))

    M = int(input())
    changed = []
    for _ in range(M):
        changed.append(list(map(int, input().split())))