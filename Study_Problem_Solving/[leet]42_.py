import collections

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def solution(root):
    if root is None:
        return 0
    queue = collections.deque([root])
    depth = 0

    while queue:
        depth += 1
        #queue 연산 추출 노드의 자식 노드 삽입
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
    return depth