class Solution:
    def trap(self, height: List[int]) -> int:
        right = len(height) -1
        left = 0
        leftMax = 0
        rightMax = 0
        water = 0

        while left<right:
            
            if height[left] < height[right]:
                if leftMax < height[left]:
                    leftMax = height[left]
                water += (leftMax - height[left])
                left += 1
            else:
                if rightMax < height[right]:
                    rightMax = height[right]
                water += (rightMax - height[right])
                right -= 1
        
        return water