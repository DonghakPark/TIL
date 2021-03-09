"""
벡터 매칭 문제
Author : DongHak Park
Contact : donghark03@naver.com
"""
import math, sys, itertools
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    N = int(input())

    point = []
    total_x = 0
    total_y = 0

    for _ in range(N):
        x, y = list(map(int, input().split()))
        point.append([x,y])
        total_x += x
        total_y += y

    ret = sys.maxsize
    com = list(itertools.combinations(point, int(N/2)))
    com_len = int(len(com)/2)

    for element in com[:com_len]:
        element = list(element)

        x1_total = 0
        y1_total = 0
        for x1, y1 in element:
            x1_total += x1
            y1_total += y1

        x2_total = total_x - x1_total
        y2_total = total_y - y1_total

        ret = min(ret, math.sqrt((x1_total - x2_total) ** 2 + (y1_total - y2_total) ** 2))
    print(ret)