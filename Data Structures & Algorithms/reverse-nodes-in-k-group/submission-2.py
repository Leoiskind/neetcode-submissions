# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseList(l, prevTail=None, k=0):
            tail = l
            curr = l
            prev = None
            for i in range(k):
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            if prevTail:
                prevTail.next = prev
            return tail

        divisors = []
        curr = head
        tally = 0
        while curr:
            if tally%k == 0:
                divisors.append(curr)
            tally += 1
            curr = curr.next
        
        findHead = head
        for i in range(k-1):
            if findHead:
                findHead = findHead.next

        prev = None
        if tally%k == 0:
            for i in range(len(divisors)):
                prev = reverseList(divisors[i], prev, k)
        else:
            for i in range(len(divisors)-1):
                prev = reverseList(divisors[i], prev, k)
            prev.next = divisors[-1]
    
        return findHead
        
