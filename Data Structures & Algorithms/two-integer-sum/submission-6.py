class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for i in range(len(nums)):
            remainder = target - nums[i]
            for j in range(i+1, len(nums)):
                if remainder == nums[j]:
                    indices.append(i)
                    indices.append(j)
                    indices.sort()
                    return indices
            