# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        return self.recursiveInvert(None, head)
    
    def recursiveInvert(self, prev, cur):
        if not cur:
            return prev
        
        nxt = cur.next
        cur.next = prev

        return self.recursiveInvert(cur, nxt)