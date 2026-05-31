# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        cur = head

        # 1 -> 2 -> 3 -> None
        
        # 3 -> 2 -> 1 -> None

        while cur:
            nxt = cur.next
            cur.next = prev            
            prev = cur
            cur = nxt
        
        return prev