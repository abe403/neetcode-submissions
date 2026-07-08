# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None

        self.reverseNodes(root)
        
        return root
        
    def reverseNodes(self, node: Optional[TreeNode]):
        if not node:
            return
        
        node.left, node.right =  node.right, node.left

        self.reverseNodes(node.left)
        self.reverseNodes(node.right)

        return node