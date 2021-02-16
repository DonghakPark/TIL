"""
Valid Palindrome Problem
Author : donghak park
Contact: donghark03@naver.com
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        answer = False
        candidate1 = ''
        candidate2 = ''

        for element in s:
            if element.isalnum():
                candidate1 = candidate1 + element.lower()
                candidate2 = element.lower() + candidate2

        if candidate2 == candidate1:
            answer = True

        return answer


if __name__=="__main__":
    S = "race a car"
    S2 = "A man, a plan, a canal: Panama"
    solution = Solution()

    print(solution.isPalindrome(S))
    print(solution.isPalindrome(S2))
