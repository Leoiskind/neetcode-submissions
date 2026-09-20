class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if num-1 in numSet:
                pass
            else:
                tally = 1
                while num + tally in numSet:
                    tally += 1
                if longest < tally:
                    longest = tally
        
        return longest