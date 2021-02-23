"""
Reverse Linked List Problem
Author : DongHak Park
Contact: donghark03@naver.com
"""

class ListNode:
    val = 0
    next = None

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        now = head
        temp = None
        while now:
            nx, now.next = now.next, temp
            temp, now = now, nx

        return temp

