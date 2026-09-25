class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMin(nums: List[int]) -> int:
            right = len(nums) -1
            left = 0
            while right > left:
                mid = (right + left)//2
                if nums[mid] <= nums[right]:
                    right = mid
                else:
                    left = mid + 1
            return left

        pivot = findMin(nums)
        print(nums[pivot])
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) //2
            print(nums[(mid + pivot) % len(nums)])
            if nums[(mid + pivot) % len(nums)] == target:
                return (mid + pivot) % len(nums)
            elif nums[(mid + pivot) % len(nums)] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1


