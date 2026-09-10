class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()
        for i in nums:
            if i not in duplicates:
                duplicates.add(i)
            else:
                return True
        return False