import heapq as hq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        cooldowns = {}
        cooldownqueue = deque()
        max_heap = []
        hq.heapify(max_heap)
        for char in tasks:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        
        for char in counts:
            hq.heappush(max_heap, [-counts[char], char])
        
        time = 0
        while max_heap or cooldownqueue:
            time += 1
            if max_heap:
                char = hq.heappop(max_heap)[1]
                counts[char] -= 1
                cooldowns[char] = time + n
                if counts[char] > 0:
                    cooldownqueue.append(char)
            if cooldownqueue and cooldowns[cooldownqueue[0]] <= time:
                charQ = cooldownqueue.popleft()
                hq.heappush(max_heap, [-counts[charQ], charQ])
        
        return time
                



        
