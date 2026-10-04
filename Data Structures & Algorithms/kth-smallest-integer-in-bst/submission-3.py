# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if not root:
            return None
        
        self.count = 0

        self.answer = -1

        def dfs(node):

            if not node:
                return None

            dfs(node.left)

            if self.count < k:
                self.answer = node.val
                self.count += 1
            else:
                return None

            dfs(node.right)
        
        dfs(root)

        return self.answer