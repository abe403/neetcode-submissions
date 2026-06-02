# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0

        def maxSearch(node):
            if not node:
                return 0

            leftBest = maxSearch(node.left)
            rightBest = maxSearch(node.right)

            self.best = max(self.best, leftBest + rightBest)
            return 1 + max(leftBest, rightBest)
        
        maxSearch(root)
        return self.best