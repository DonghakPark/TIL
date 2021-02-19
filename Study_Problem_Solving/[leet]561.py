"""
Array Partition 1
Author : DongHak Park
contact: donghark03@naver.com
"""
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        answer = 0

        for first in range(0,len(nums),2):
            answer += nums[first]

        return answer


if __name__ == "__main__":
    solution = Solution()

    nums1 = [1,4,3,2]
    nums2 = [6,2,6,5,1,2]

    print(solution.arrayPairSum(nums1))
    print(solution.arrayPairSum(nums2))


