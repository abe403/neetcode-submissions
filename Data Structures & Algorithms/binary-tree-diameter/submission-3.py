# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    best = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.maxSearch(root)

        return self.best
        
    
    def maxSearch(self, node):

        if not node:
            return 0
        
        leftBest = self.maxSearch(node.left)
        rightBest = self.maxSearch(node.right)

        self.best = max(self.best, leftBest + rightBest)

        return 1 + max(leftBest, rightBest)
