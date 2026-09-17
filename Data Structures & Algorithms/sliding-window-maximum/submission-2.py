class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq as hq
        maxPerWindow = []
        maxNum = - float('inf')
        heap = []
        for i in range(k-1):
            hq.heappush(heap, (-nums[i], i))
        
        right = k-1
        while right < len(nums):
            hq.heappush(heap, (-nums[right], right))
            while heap[0][1] <= right - k:
                hq.heappop(heap)
            
            maxNum =  - heap[0][0]
            maxPerWindow.append(maxNum)

            right +=1
        
        return maxPerWindow