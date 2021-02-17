"""
Longest Palindromic Substring Problem
Author : Donghak Park
Contact: donghark03@naver.com
"""


class Solution:

    def is_Palindrome(self, s: str, start: int, end: int) -> str:
        while start >= 0 and end <= len(s):
            if s[start] == s[end - 1]:
                start -= 1
                end += 1
            else:
                break

        return s[start + 1:end - 1]

    def longestPalindrome(self, s: str) -> str:

        if len(s) < 2 or s == s[::-1]:
            return s

        answer = ''

        for i in range(len(s) - 1):
            answer = max(answer,
                         self.is_Palindrome(s, i, i + 1),
                         self.is_Palindrome(s, i, i + 2),
                         key=len)

        return answer


if __name__ == "__main__":
    solution = Solution()
    s = "abb"
    print(solution.longestPalindrome(s))
