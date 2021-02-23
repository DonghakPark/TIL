"""
Reverse Linked List 2 Problem
Author : DongHak Park
Contact: donghark03@naver.com
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left==right:
            return head

        root = start = ListNode(None)
        root.next = head

        for _ in range(left - 1):
            start = start.next
        end = start.next

        for _ in range(right-left):
            temp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = temp

        return root.next

if __name__=="__main__":
    print("______________start________________")
    solution = Solution()

    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4, ListNode(5,None)))))
    left, right = 2, 4

    ret = solution.reverseBetween(head, left, right)

    now = ret
    while now:
        print(now.val, end = " ")
        now = now.next
    print()
    print("________________end________________")