"""
Reorder Data in Log Files Problem
Author : donghak Park
Contact: donghark03@naver.com
"""
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        for element in logs:
            if element.split()[1].isdigit():
                digit_logs.append(element)
            else:
                letter_logs.append(element)

        letter_logs.sort(key = lambda x:(x.split()[1:], x.split()[0]))

        for element in digit_logs:
            letter_logs.append(element)

        return letter_logs


if __name__=="__main__":
    solution = Solution()
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    print(solution.reorderLogFiles(logs))