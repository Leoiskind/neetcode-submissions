class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.capacity = capacity
        self.cache = {} 

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Detach
            node.prev.next = node.next
            node.next.prev = node.prev
            # Replace
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            return node.val[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = (key, value)
            # Detach
            node.prev.next = node.next
            node.next.prev = node.prev
            # Replace
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
        else:
            if len(self.cache) >= self.capacity:
                if self.tail.prev == self.head:
                    pass
                else:   
                    # Remove oldest
                    oldNode = self.tail.prev
                    self.cache.pop(oldNode.val[0])
                    oldNode.prev.next = oldNode.next
                    oldNode.next.prev = oldNode.prev
                
            
            # implement new node
            node = Node((key, value), self.head, self.head.next)
            self.cache[key] = node
            self.head.next.prev = node
            self.head.next = node