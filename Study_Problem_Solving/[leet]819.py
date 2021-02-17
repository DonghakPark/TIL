"""
Most Common Word Problem
Author : donghak park
Contact: donghark03@naver.com
"""
from typing import List
import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned : List[str]) -> str:

        para_list = [s for s in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                     if s not in banned]

        counts = Counter(para_list)
        answer = counts.most_common(1)[0][0]
        return answer


if __name__=="__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    solution = Solution()
    print(solution.mostCommonWord(paragraph, banned))