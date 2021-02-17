"""
Two Sum Problem
Author : donghak park
Contact: donghark03@naver.com
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    answer = [i, j]
                    break
        return answer

    def twoSum_binary_Search(self, nums: List[int], target: int) -> List[int]:
        #index를 찾는 경우가 아닌 경우만 사용가능
        nums.sort()

        left, right = 0, len(nums) - 1
        while not left == right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]

if __name__=="__main__":
    nums = [2,7,11,15]
    target = 9

    solution = Solution()
    print(solution.twoSum(nums, target))