"""
야근 지수 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""

import heapq


def solution(n, works):
    answer = 0

    Q = []

    for element in works:
        heapq.heappush(Q, -element)

    count = 0
    while count < n:
        if Q:
            now = heapq.heappop(Q)
            now += 1
            if now == 0:
                count += 1
            else:
                heapq.heappush(Q, now)
                count += 1
        else:
            count += 1

    for element in Q:
        answer += element ** 2

    return answer