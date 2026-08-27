class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        for i in range(len(nums)):
            if nums[i] in duplicates:
                print(nums[i])
                return True
            else:
                duplicates[nums[i]] = 0
        return False