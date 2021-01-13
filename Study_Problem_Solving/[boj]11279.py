"""
최대 힙 문제
author : donghak park
contact : donghark03@naver.com
"""

import heapq
import sys
input = sys.stdin.readline

N = int(input())
Q = []

for _ in range(N):
    x = int(input())

    if x == 0:
        if Q:
            print(-heapq.heappop(Q))
        else:
            print(0)
    else:
        heapq.heappush(Q, -x)
