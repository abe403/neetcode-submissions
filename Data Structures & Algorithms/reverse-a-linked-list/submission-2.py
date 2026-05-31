# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return ListNode().next

        cur = head    

        saved = []

        while cur:
            saved.append(cur.val)
            cur = cur.next
        
        dummy = ListNode(0)
        cur = dummy

        for n in range(len(saved) - 1, -1, -1):
            cur.next = ListNode(saved[n])
            cur = cur.next

        return dummy.next