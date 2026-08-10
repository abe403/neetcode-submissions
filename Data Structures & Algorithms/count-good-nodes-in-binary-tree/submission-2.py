# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        return self.countGoodNodesInSubtree(root, root.val)
    
    def countGoodNodesInSubtree(self, currentNode: TreeNode, maxValueSeenSoFar: int) -> int:

        if not currentNode:
            return 0
        
        if currentNode.val >= maxValueSeenSoFar:
            good = 1
        else:
            good = 0
        
        maxValueSeenSoFar = max(maxValueSeenSoFar, currentNode.val)

        leftGoodNodeCount = self.countGoodNodesInSubtree(currentNode.left, maxValueSeenSoFar)

        rightGoodNodeCount = self.countGoodNodesInSubtree(currentNode.right, maxValueSeenSoFar)

        return good + leftGoodNodeCount + rightGoodNodeCount