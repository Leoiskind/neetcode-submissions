class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        largest = 0
        for num in nums:
            numSet.add(num)
        
        for num in numSet:
            if num-1 not in numSet:
                tally = 0
                while num+tally in numSet:
                    tally+=1
                if tally>largest:
                    largest = tally
        
        return largest
