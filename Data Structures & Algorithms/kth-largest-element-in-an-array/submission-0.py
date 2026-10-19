import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-x for x in nums]
        hq.heapify(maxheap)
        for i in range(k-1):
            hq.heappop(maxheap)

        return -hq.heappop(maxheap)