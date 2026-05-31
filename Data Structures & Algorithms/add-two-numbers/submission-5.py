# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0

        l1cur = l1
        l2cur = l2

        head = None
        cur = None
        isFirst = True

        while l1cur or l2cur or carry > 0:
            l1value = l1cur.val if l1cur else 0
            l2value = l2cur.val if l2cur else 0

            total = l1value + l2value + carry
            digit = total % 10
            carry = total // 10

            new_node = ListNode(digit)

            if isFirst:
                head = new_node
                cur = new_node
                isFirst = False
            else:
                cur.next = new_node
                cur = cur.next

            if l1cur:
                l1cur = l1cur.next

            if l2cur:
                l2cur = l2cur.next

        return head