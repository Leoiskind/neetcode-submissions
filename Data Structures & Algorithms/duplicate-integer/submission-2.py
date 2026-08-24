class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        itemSet = set() # This correctly creates an empty set
        for i in nums:
            if i in itemSet:
                return True
            else:
                itemSet.add(i)
        return False