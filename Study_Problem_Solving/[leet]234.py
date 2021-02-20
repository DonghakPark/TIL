"""
Palindrome Linked List
Author : DongHak Park
Contact: donghark03@naver.com
"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        Arr = []

        if head is None:
            return True

        while head.next != None:
            Arr.append(head.val)
            head = head.next

        Arr.append(head.val)

        if Arr == Arr[::-1]:
            return True
        else:
            return False

if __name__=="__main__":
    solution = Solution()

    head = ListNode(1,ListNode(2, None))
    print(solution.isPalindrome(head))