"""
Merge Two Sorted Lists
Author : DongHak Park
Contact: donghark03@naver.com
TODO : 못풀었음
"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 is None and l2 is not None:
            return l2
        elif l1 is not None and l2 is None:
            return l1
        elif l1 is None and l2 is None:
            return []




if __name__=="__main__":
    solution = Solution()
    l1 = ListNode(1, ListNode(2, ListNode(4, None)))
    l2 = ListNode(1, ListNode(3, ListNode(4, None)))
    print(solution.mergeTwoLists(l1,l2))