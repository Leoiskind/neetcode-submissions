class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = [[] for i in range(len(nums) + 1)]
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        for key in counts:
            frequencies[counts[key]].append(key)
        
        res = []
        for i in range(len(frequencies) -1, 0, -1):
            for n in frequencies[i]:
                res.append(n)
                if len(res) == k:
                    return res