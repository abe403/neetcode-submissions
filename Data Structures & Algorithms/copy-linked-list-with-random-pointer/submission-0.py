"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        val = {}

        cur = head

        while cur:
            val[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head

        while cur:
            copy = val[cur]
            copy.next = val.get(cur.next)
            copy.random = val.get(cur.random)
            cur = cur.next

        return val.get(head)
