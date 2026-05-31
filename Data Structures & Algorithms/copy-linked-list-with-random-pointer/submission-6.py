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
        
        copy = {}

        cur = head

        while cur:
            copy[cur] = Node(cur.val)
            cur = cur.next

        cur = head

        while cur:
            copy[cur].next = copy.get(cur.next)
            copy[cur].random = copy.get(cur.random)
            cur = cur.next

        return copy.get(head)

