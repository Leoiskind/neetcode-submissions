import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneheap = [-x for x in stones]
        hq.heapify(stoneheap)
        while len(stoneheap) > 1:
            x = -hq.heappop(stoneheap)
            y = -hq.heappop(stoneheap)
            diff = x - y
            if diff != 0:
                hq.heappush(stoneheap, -diff)
        
        if stoneheap:
            return -stoneheap[0]
        
        return 0
