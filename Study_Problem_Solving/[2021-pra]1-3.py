"""
2021 상반기 코딩테스트 대비 연습 문제 풀이
Author : DongHak Park
Contact: donghark03@naver.com
"""
from idlelib.tree import TreeNode
from typing import List


class Solution:
    def preorder(self, head: TreeNode, arr: List) -> None:
        if head is None:
            arr.append(0)
            return

        arr.append(head.val)
        self.preorder(head.left, arr)
        self.preorder(head.right, arr)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_preorder = []
        q_preorder = []

        self.preorder(p, p_preorder)
        self.preorder(q, q_preorder)

        return p_preorder == q_preorder
