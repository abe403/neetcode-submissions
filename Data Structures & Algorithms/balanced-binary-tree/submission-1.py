# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    isTreeBalanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        self.countHeight(root)

        return self.isTreeBalanced

    def countHeight(self, node):
        
        if not self.isTreeBalanced:
            return False

        if not node:
            return 0
        
        leftHeight = self.countHeight(node.left)
        rightHeight = self.countHeight(node.right)

        if (abs(leftHeight - rightHeight)) >= 2:
            self.isTreeBalanced = False
        
        return 1 + max(leftHeight, rightHeight)        
        