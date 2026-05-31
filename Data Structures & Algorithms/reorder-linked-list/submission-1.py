# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        prev = None
        cur = slow.next
        slow.next = None  # cut the list in half

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # Now:
        # first half starts at head
        # reversed second half starts at prev

        # 3. Merge both halves alternating
        first = head
        second = prev

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2