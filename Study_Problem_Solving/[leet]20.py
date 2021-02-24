"""
Valid Parentheses
Author : DongHak Park
Contact: donghark03@naver.com
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        a = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        s = list(s)
        while s:
            temp = s.pop(0)
            if stack and (temp in a.keys()):
                if a[temp] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(temp)
            else:
                stack.append(temp)
        if stack:
            return False
        else:
            return True


if __name__ == "__main__":
    solution = Solution()
    s = "(])"
    print(solution.isValid(s))
