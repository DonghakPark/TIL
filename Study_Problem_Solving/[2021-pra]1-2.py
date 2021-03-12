"""
2021 상반기 코딩테스트 대비 연습 문제 풀이
Author : DongHak Park
Contact: donghark03@naver.com
"""
from typing import List


# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         answer = 0
#
#         length = len(height)
#
#         for i in range(length):
#             for j in range(length):
#                 if i == j:
#                     continue
#                 else:
#                     width = abs(j - i)
#                     height_in = min(height[i], height[j])
#                     answer = max(answer, width * height_in)
#
#         return answer


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        answer = 0

        while start <= end:
            w = end - start
            if height[start] > height[end]:
                h = height[end]
                answer = max(answer, w * h)
                end -= 1
            else:
                h = height[start]
                answer = max(answer, w * h)
                start += 1
        return answer
