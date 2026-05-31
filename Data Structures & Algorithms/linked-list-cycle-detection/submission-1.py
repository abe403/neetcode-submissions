# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        cur = head

        seen = {}

        while cur:
            if cur in seen:
                return True
            else:
                seen[cur] = True
                cur = cur.next
                
        return False