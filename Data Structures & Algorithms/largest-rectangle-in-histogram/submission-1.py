class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        bigArea=0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop(-1)
                left = stack[-1] if stack else -1
                area = (i-left-1) * heights[idx]
                if bigArea < area:
                    bigArea = area
            stack.append(i)
        
        while stack:
            idx = stack.pop(-1)
            left = stack[-1] if stack else -1
            area = (len(heights)-left-1) * heights[idx]
            if bigArea < area:
                bigArea = area
        return bigArea