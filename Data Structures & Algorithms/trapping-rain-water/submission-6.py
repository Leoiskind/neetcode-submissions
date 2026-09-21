class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        water = 0
        maxLeft = max(0, height[left])
        maxRight = max(0, height[right])

        while right > left:
            if height[right] < height[left]:
                heightM = min(maxRight, maxLeft)
                waterGain = heightM - height[right] if heightM - height[right] > 0 else 0
                water += waterGain
                right -= 1
                maxRight = max(maxRight, height[right])
            else:
                heightM = min(maxRight, maxLeft)
                waterGain = heightM - height[left] if heightM - height[left] > 0 else 0
                water += waterGain
                left += 1
                maxLeft = max(maxLeft, height[left])
        
        return water