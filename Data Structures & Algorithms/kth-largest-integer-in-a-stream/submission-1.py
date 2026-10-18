import heapq as hq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        hq.heapify(self.heap)
        while len(self.heap) > self.k:
            hq.heappop(self.heap)

    def add(self, val: int) -> int:
        hq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            hq.heappop(self.heap)
        return self.heap[0]