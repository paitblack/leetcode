# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode()
        current = dummy_head
        carry = 0 

        while l1 or l2:
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            
            sum_val = val1 + val2 + carry
            carry = sum_val // 10
            digit = sum_val % 10  

            current.next = ListNode(digit)
            current = current.next 

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy_head.next
        
        