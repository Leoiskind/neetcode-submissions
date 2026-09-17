# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
        curr = mid.next
        mid.next = None
        prev = None

        while curr:
            post = curr.next
            curr.next = prev
            prev = curr
            curr = post
        
        head2 = prev

        dummy = ListNode()
        while head and head2:
            dummy.next = head
            head = head.next
            dummy = dummy.next
            dummy.next = head2
            head2 = head2.next
            dummy = dummy.next
        
        while head:
            dummy.next = head
            head = head.next
            dummy = dummy.next
        
        return dummy.next

