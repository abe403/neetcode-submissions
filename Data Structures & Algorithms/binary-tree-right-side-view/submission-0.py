# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        queue = deque([root])

        ans = []

        node = root

        while queue:

            lvl = []

            lvlsize = len(queue)

            for n in range(lvlsize):

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                lvl.append(node.val)
            
            ans.append(lvl.pop())
        
        return ans
            

