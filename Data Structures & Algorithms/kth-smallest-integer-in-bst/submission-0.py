# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        curPath = []
        node = root

        while curPath or node:
            while node:
                curPath.append(node)
                node = node.left
            
            node = curPath.pop()
            k -=1
            if k == 0:
                return node.val
            node = node.right

            #          10
            #       8     13
            #      7 9  14  15
        
