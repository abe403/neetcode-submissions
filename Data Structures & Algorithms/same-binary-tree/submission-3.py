# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    isSame = True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        self.isNodeSame(p, q)

        return self.isSame

    def isNodeSame(self, p, q):

        if not p:
            if q:
                self.isSame = False
            return

        if not q:
            if p:
                self.isSame = False
            return

        if ( p.val != q.val ):
            self.isSame = False

        self.isSameTree(p.left, q.left)
        self.isSameTree(p.right, q.right)

        return