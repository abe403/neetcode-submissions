# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        self.maxSearch(root)

        return self.best
    
    def maxSearch(self, node):

        if not node:
            return 0
        
        leftHeight = self.maxSearch(node.left)
        rightHeight = self.maxSearch(node.right)

        self.best = max(self.best, leftHeight + rightHeight)

        return 1 + max(leftHeight, rightHeight)
