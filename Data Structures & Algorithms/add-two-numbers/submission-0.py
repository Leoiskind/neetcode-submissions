# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummy = dummyHead
        carry = 0

        while l1 and l2:
            sm = l1.val + l2.val + carry
            numerator = sm %10
            carry = sm //10
            dummy.next = ListNode(numerator)
            l1 = l1.next
            l2 = l2.next
            dummy = dummy.next
        
        if l1:
            while l1:
                sm = carry + l1.val
                numerator = sm %10
                carry = sm // 10
                dummy.next = ListNode(numerator)
                dummy = dummy.next
                l1 = l1.next
        if l2:
            while l2:
                sm = carry + l2.val
                numerator = sm %10
                carry = sm // 10
                dummy.next = ListNode(numerator)
                dummy = dummy.next
                l2 = l2.next 
        
        if carry>0:
            dummy.next = ListNode(carry)
        
        return dummyHead.next               

