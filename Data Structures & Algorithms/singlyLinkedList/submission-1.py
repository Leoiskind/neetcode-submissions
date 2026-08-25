class LinkedList:
    
    def __init__(self):
        self.linkedList = []
    
    def get(self, index: int) -> int:
        if index < len(self.linkedList):
            return self.linkedList[index]
        else:
            return -1

    def insertHead(self, val: int) -> None:
        newList = []
        newList.append(val)
        for i in self.linkedList:
            newList.append(i)
        self.linkedList = newList

    def insertTail(self, val: int) -> None:
        self.linkedList.append(val)

    def remove(self, index: int) -> bool:
        if index < len(self.linkedList):
            self.linkedList.pop(index)
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        return self.linkedList
