# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = root.val

        def build(node):
            nonlocal res
            if not node:
                return 0
            
            max_left = max(0, build(node.left))
            max_right = max(0, build(node.right))

            res = max(res, max_left + node.val + max_right)

            return node.val + max(max_left, max_right)
        
        build(root)

        return res

