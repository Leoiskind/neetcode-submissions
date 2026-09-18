"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {}
        dummyHead = Node(1)
        dummy = dummyHead
        curr = head
        while curr:
            dummy.next = Node(curr.val)
            mapping[curr] = dummy.next
            dummy = dummy.next
            curr = curr.next
        
        dummy = dummyHead
        curr = head
        while curr:
            if not curr.random:
                dummy.next.random = None
            else:
                dummy.next.random = mapping[curr.random]
            dummy = dummy.next
            curr = curr.next
        
        return dummyHead.next
