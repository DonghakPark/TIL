"""
Jewels and Stones Problem
Author : DongHak Park
Contact: donghark03@naver.com
"""
import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        stone_dict = collections.defaultdict(int)
        answer = 0

        for i in range(len(stones)):
            stone_dict[stones[i]] += 1

        for i in range(len(jewels)):
            answer += stone_dict[jewels[i]]

        return answer


if __name__=="__main__":
    solution = Solution()
    jewels = 'aA'
    stones = 'aAAbbbb'
    print(solution.numJewelsInStones(jewels,stones))
