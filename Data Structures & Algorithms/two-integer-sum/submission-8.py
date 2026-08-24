class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainderMap = {}
        indices = []
        for i in range(len(nums)):
            remainder = target - nums[i]
            if(remainder in remainderMap):
                indices.append(i)
                indices.append(remainderMap[remainder])
                indices.sort()
                return indices
            remainderMap[nums[i]] = i