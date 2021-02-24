"""
Remove Duplicate Letters
Author : DongHak Park
Contact: donghark03@naver.com
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            char = s[i]
            flag = True
            for j in range(0, i):
                if s[j] < char:
                   flag = False


        return "".join(stack)

if __name__=="__main__":
    solution = Solution()
    s = "cbacdcbc"
    print(solution.removeDuplicateLetters(s))