"""
다각형의 면적 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""
from collections import deque
import math


def ccw(x1, y1, x2, y2, x3, y3):
    return (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)


N = int(input())
x, y = map(int, input().split())

position = deque()
for _ in range(N-1):
    position.append(list(map(int, input().split())))

answer = 0
for i in range(N-2):
    answer += ccw(x, y,
                  position[i][0], position[i][1],
                  position[i+1][0], position[i+1][1])

print(round(abs(answer)/2, 1))

# 삼각형 높이 구하는 공식
# if len(triangle) == 3:
#     point_1 = triangle.popleft()
#     point_2 = triangle[0]
#     point_3 = triangle[1]
#     if (point_3[0] - point_2[0]) != 0:
#         a = (point_3[1] - point_2[1])/(point_3[0] - point_2[0])
#         c = point_2[1] - ( a * point_2[0] )
#         h = abs(a*point_1[0] + -1 * point_1[1] + c) / (math.sqrt(a ** 2 + 1))
#     else:
#         h = abs(point_3[1] - point_2[1])
#     w = math.sqrt((point_3[1] - point_2[1]) ** 2 + (point_3[0] - point_2[0]) ** 2)
#     answer += (h*w)/2
