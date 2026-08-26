class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        
        sortedNums = sorted(frequencies, key=frequencies.get, reverse=True)

        returned = []
        for i in range(k):
            returned.append(sortedNums[i])
        
        return returned