class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums) -1
        left = 0
        mid = 0
        lowest = nums[0]
        while right >= left:
            mid = (right + left)//2
            print(nums[mid])
            lowest = min(nums[mid], lowest)
            if nums[mid] <= nums[right]:
                right = mid-1
            else:
                left = mid+1
        return lowest