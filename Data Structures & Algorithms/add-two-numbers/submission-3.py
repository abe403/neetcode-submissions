# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0

        dummy = ListNode(0)

        l1cur = l1
        l2cur = l2

        cur = dummy

        while l1cur or l2cur or carry != 0:
            
            l1value = l1cur.val if l1cur else 0

            l2value = l2cur.val if l2cur else 0
            
            numsum = (l1value + l2value + carry) % 10
            carry = (l1value + l2value + carry) // 10

            cur.next = ListNode(numsum)
            cur = cur.next
            if l1cur:
                l1cur = l1cur.next 
            if l2cur:
                l2cur = l2cur.next
        
        return dummy.next