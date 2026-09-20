class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i] -1 in numSet:
                pass
            else:
                tally = 1
                while nums[i] + tally in numSet:
                    tally += 1
                if longest < tally:
                    longest = tally
        
        return longest