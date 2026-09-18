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
        curr = head
        while curr:
            dummy = Node(curr.val)
            mapping[curr] = dummy
            curr = curr.next
        
        dummy = dummyHead
        curr = head
        while curr:
            dummy.next = mapping[curr]
            dummy = dummy.next
            if not curr.random:
                dummy.random = None
            else:
                dummy.random = mapping[curr.random]
            
            dummy.val = curr.val
            curr = curr.next
        
        return dummyHead.next
                
