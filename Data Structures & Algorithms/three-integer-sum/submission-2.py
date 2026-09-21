class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pointer = 0
        triplets = set()
        nums.sort()
        while pointer < len(nums):
            left = pointer + 1
            right = len(nums) - 1
            target = -nums[pointer]
            while right > left:
                summed = nums[right] + nums[left]
                if summed == target:
                    triplet = [nums[right], nums[left], nums[pointer]]
                    triplet.sort()
                    triplets.add(tuple(triplet))
                    left += 1
                elif summed < target:
                    left += 1
                else:
                    right -= 1
                
            pointer += 1
            
        return list(triplets)