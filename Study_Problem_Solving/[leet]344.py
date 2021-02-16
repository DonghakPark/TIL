"""
Reverse String Problem
Author : donghak park
Contact: donghark03@naver.com
"""


class Solution:
    def reverseString(self, s) -> None:
        s.reverse()


if __name__=="__main__":
    solution = Solution()
    s = ["h","e","l","l","o"]
    solution.reverseString(s)
    print(s)
