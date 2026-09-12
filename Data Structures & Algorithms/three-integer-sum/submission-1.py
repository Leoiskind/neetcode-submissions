class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left = 0
        right = len(nums) -1
        sortNums = sorted(nums)
        trios = set()
        for i in range(len(sortNums)):
            target = -sortNums[i]
            left = i+1
            right = len(nums) -1
            while left < right:
                summed = sortNums[left] + sortNums[right]
                if summed == target:
                    trios.add((sortNums[i], sortNums[left], sortNums[right]))
                    left+=1
                elif summed<target:
                    left+=1
                else:
                    right-=1
        return list(trios)