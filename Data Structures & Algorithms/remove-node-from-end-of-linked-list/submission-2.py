# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        length = 0
        dummy = head
        while dummy:
            dummy = dummy.next
            length += 1
        
        print(length - n)
        if length == n:
            head = head.next
            return head
        
        curr = head
        for i in range(length - n -1):
            curr = curr.next
        
        if curr.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        
        return head