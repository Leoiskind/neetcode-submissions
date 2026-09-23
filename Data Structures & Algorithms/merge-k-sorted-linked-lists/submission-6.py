# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeLists(l1, l2):
            dummyHead = ListNode()
            dummy = dummyHead
            while l1 and l2:
                if l1.val < l2.val:
                    dummy.next = l1
                    l1 = l1.next
                    dummy = dummy.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                    dummy = dummy.next
            if l1:
                dummy.next = l1
            elif l2:
                dummy.next = l2
            
            return dummyHead.next
        
        newList = lists
        while len(newList) > 1:
            tempList = []
            for i in range(0, len(newList), 2):
                if i+1 < len(newList):
                    tempList.append(mergeLists(newList[i], newList[i+1]))
                else:
                    tempList.append(newList[i])
            
            newList = tempList
        
        if newList:
            return newList[0]
        else:
            return None

