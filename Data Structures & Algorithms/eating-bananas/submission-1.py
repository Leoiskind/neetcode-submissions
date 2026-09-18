class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        right = max(piles)
        left = 1
        lowest = right
        while left <= right:
            mid = (right + left) // 2
            eatingTime = 0
            for i in range(len(piles)):
                eatingTime += math.ceil(piles[i] / mid)
            print(mid)
            print(eatingTime)
            print(eatingTime <= h)
            if eatingTime <= h:
                if lowest > mid:
                    lowest = mid
                right = mid -1
            else:
                left = mid + 1
        
        return lowest