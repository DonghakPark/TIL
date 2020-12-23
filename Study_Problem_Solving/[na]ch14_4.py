"""
카드 정렬하기 문제
author : donghak park
contact : donghark03@naver.com
"""
import heapq

N = int(input())
arr = []
for i in range(N):
    heapq.heappush(arr, (int(input())))

answer = 0
while len(arr) > 1:
    A = heapq.heappop(arr)
    B = heapq.heappop(arr)
    heapq.heappush(arr, A+B)

    answer += A + B

print(answer)