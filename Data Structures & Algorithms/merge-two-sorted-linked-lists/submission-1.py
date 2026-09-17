# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
    
        if list1.val <= list2.val:
            head = list1
            head2 = list2
        else:
            head = list2
            head2 = list1
        

        curr = head
        while curr:
            if not curr.next:
                if not head2:
                    return head
                else:
                    post = curr.next
                    curr.next = head2
                    head2 = post
                    curr = curr.next
            elif not head2:
                return head
            elif curr.next.val <= head2.val:
                curr = curr.next
            else:
                post = curr.next
                curr.next = head2
                curr = curr.next
                head2 = post
        
        return head