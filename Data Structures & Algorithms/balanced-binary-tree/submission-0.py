# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.Balanced = True
        def maxHeight(node):
            if not node:
                return 0

            maxLeft = maxHeight(node.left)
            maxRight = maxHeight(node.right)

            if abs(maxRight - maxLeft) > 1:
                self.Balanced = False

            return 1 + max(maxLeft, maxRight)
        
        maxHeight(root)
        return self.Balanced
        
