"""
Longest Substring Without Repeating Characers Problem
Author : DongHak Park
Contact: donghark03@naver.com
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            if (char in used) and (start <= used[char]):
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)
            used[char] = index
        return max_length


if __name__=="__main__":
    solution = Solution()
    s = "pwwkew"
    print(solution.lengthOfLongestSubstring(s))