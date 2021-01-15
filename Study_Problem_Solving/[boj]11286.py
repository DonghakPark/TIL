"""
절댓값 힙 문제
author : donghak park
contact: donghark03@naver.com
"""
import heapq
import sys
input = sys.stdin.readline

N = int(input())
Q = []

for _ in range(N):
    num = int(input())


    if num != 0:
        if num < 0:
            heapq.heappush(Q, [abs(num),-1])
        else:
            heapq.heappush(Q, [abs(num), 1])
    else:
        if Q:
            temp, oper = heapq.heappop(Q)
            print(temp*oper)
        else:
            print(0)
