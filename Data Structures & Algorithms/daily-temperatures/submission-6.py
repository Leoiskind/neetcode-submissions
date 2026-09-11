class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, j in enumerate(temperatures):
            if stack:
                target = stack[-1]
                while stack and j>stack[-1][1]:
                    idx, temp = stack.pop(-1)
                    result[idx] = i - idx
            stack.append((i, j))
        return result