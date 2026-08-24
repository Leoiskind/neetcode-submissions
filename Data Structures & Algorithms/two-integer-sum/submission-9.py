class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainderMap = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if(remainder in remainderMap):
                return [remainderMap[remainder], i]
            remainderMap[nums[i]] = i