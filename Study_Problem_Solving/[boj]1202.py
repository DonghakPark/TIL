"""
보석 도둑 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""
import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())
Q = []

jew = [list(map(int, input().split())) for _ in range(N)]
bag = [int(input()) for _ in range(K)]

jew.sort(key = lambda x: x[0])
bag.sort()

answer = 0
index = 0
for now in bag:
    while index < N and now >= jew[index][0]:
        heapq.heappush(Q, -jew[index][1])
        index += 1
    if Q:
        answer -= heapq.heappop(Q)

print(answer)