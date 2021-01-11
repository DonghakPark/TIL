"""
최소 힙 문제
author : donghak park
contact : donghark03@naver.com
"""

import sys
import heapq
input = sys.stdin.readline

N = int(input())
Q = []
for _ in range(N):
    temp = int(input())

    if temp > 0 :
        heapq.heappush(Q, temp)
    elif temp == 0:
        if len(Q) != 0:
            print(heapq.heappop(Q))
        elif len(Q) == 0:
            print(0)
