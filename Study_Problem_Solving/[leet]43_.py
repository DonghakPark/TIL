class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class solution:
    def __init__(self):
        pass

    longest = 0

    def dfs(self, node):
        if not node:
            return -1
        left = solution.dfs(node.left)
        right = solution.dfs(node.right)

        self.longest = max(self.longest, left+right+2)

        return max(left,right) +1

