# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isBinary(node: Optional[TreeNode], minimum: int, maximum: int) -> int:

            if not node:
                return True

            if not (minimum < node.val < maximum):
                return False
            
            leftValid = isBinary(node.left, minimum, node.val)

            rightValid = isBinary(node.right, node.val, maximum)

            return leftValid and rightValid
        
        return isBinary(root, float("-inf"), float("inf"))

    