"""
Top K Frequent Elements Problem
Author : DongHak Park
Contact: donghark03@naver.com
"""
from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for c in count:
            heapq.heappush(heap, (-count[c], c))
        answer = []
        for _ in range(k):
            answer.append(heapq.heappop(heap)[1])

        return answer


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(solution.topKFrequent(nums, k))
