class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA=0
        left = 0
        right = len(heights) -1
        while left<right:
            area = min(heights[left], heights[right]) * (right-left)
            print(area)
            if area>maxA:
                maxA=area
            if heights[right] < heights[left]:
                right-=1
            else:
                left+=1

        return maxA