class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums) -1
        left = 0
        while right > left:
            mid = (right + left)//2
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid+1
        return nums[left]