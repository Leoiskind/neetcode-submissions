class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = []
        backward = []
        num = 1
        num2 = 1
        for i in range(len(nums)):
            forward.append(num)
            backward.append(num2)
            num *= nums[i]
            num2 *= nums[-i -1]


        retList = []
        for i in range(len(nums)):
            retList.append(forward[i] * backward[-i-1])
        
        return retList