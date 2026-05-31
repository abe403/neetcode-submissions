# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        cur = second

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # 2, 4
        # 8, 6

        # slwnxt = 4
        # fstnxt = 6

        # 2 -> 8
        
        # slow = 4

        # 2 -> 8 -> 4

        # fast = 6 

        slow = head
        fast = prev

        while fast:
            slwnxt = slow.next
            fstnxt = fast.next

            slow.next = fast
            fast.next = slwnxt
            
            slow = slwnxt
            fast = fstnxt
