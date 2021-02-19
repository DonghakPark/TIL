"""
Product Of Array Except Self Problem
Author : DongHak Park
Contact: donghark03@naver.com
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        front = [1]
        end = [1]

        for i in range(len(nums)-1):
            front.append(front[-1] * nums[i])
        for i in range(len(nums)-1, 0, -1):
            end.insert(0, end[0] * nums[i])

        for i in range(len(nums)):
            answer.append(front[i] * end[i])

        return answer

if __name__=="__main__":
    solution = Solution()
    nums = [1,2,3,4]
    print(solution.productExceptSelf(nums))
