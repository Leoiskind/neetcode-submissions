import heapq as hq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        hq.heapify(dists)
        for point in points:
            hq.heappush(dists, ((-math.sqrt(point[0] ** 2 + point[1] ** 2), point)))

            if len(dists) > k:
                hq.heappop(dists)
        
        kclosest = []
        for i in range(k):
            kclosest.append(hq.heappop(dists)[1])

        return kclosest

