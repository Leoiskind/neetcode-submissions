class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        self.size += 1
        if (self.capacity < self.getSize()):
            self.resize()
        self.array[self.getSize()-1] = n
        

    def popback(self) -> int:
        temp = self.array[self.getSize() - 1]
        self.array[self.getSize()-1] = None
        self.size -= 1
        return temp


    def resize(self) -> None:
        self.capacity = self.capacity * 2
        tempArray = [None] * self.capacity
        for i in range(len(self.array)):
            tempArray[i] = self.array[i]
        self.array = tempArray

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity