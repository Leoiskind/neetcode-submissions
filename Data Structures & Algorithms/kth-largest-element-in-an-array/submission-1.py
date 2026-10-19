import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        hq.heapify(minheap)
        for i in nums:
            hq.heappush(minheap, i)
            if len(minheap) > k:
                hq.heappop(minheap)

        return hq.heappop(minheap)