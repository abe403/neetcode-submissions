# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        if not root:
            return ""

        q = deque([root])

        res = []

        while q:
        
            node = q.popleft()

            if node:
                res.append(node.val)
                
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")

        return ",".join(str(value) for value in res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        vals = data.split(",")
        root = TreeNode(int(vals[0]))

        q = deque([root])
        i = 1

        for i in range(1, len(vals), 2):

            node = q.popleft()
            left_value = vals[i]
            right_value = vals[i + 1]

            if left_value != "null":
                left_node = TreeNode(int(left_value))
                node.left = left_node
                q.append(left_node)
            if right_value != "null":
                right_node = TreeNode(int(right_value))
                node.right = right_node
                q.append(right_node)

        return root
        


