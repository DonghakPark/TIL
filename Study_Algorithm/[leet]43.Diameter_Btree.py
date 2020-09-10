class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

longest = 0
def dfs(node):
    if not node:
        return -1
    left = dfs(node.left)
    right = dfs(node.right)

    self.longest = max(self.longest, left+right+2)

    return max(left,right) +1
dfs(root)
return self.longest