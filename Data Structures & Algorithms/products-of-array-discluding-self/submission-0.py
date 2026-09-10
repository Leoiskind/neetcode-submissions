class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1] * len(nums)
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        prefix[0] = nums[0]
        postfix[-1] = nums[-1]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
            postfix[-i-1] = postfix[-i] * nums[-i-1]
        
        for i in range(len(nums)):
            if i+1<len(nums) and i-1>=0:
                product[i] = postfix[i+1] * prefix[i-1]
            elif i+1<len(nums):
                product[i] = postfix[i+1]
            elif i-1>=0:
                product[i] = prefix[i-1]
            else:
                product[i] = 1
            
        return product