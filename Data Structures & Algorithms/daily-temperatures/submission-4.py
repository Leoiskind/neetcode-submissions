class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, j in enumerate(temperatures):
            if stack:
                target = stack[-1]
                while j>target[1] and stack:
                    result[target[0]] = i - target[0]
                    stack.pop(-1)
                    if stack:
                        target = stack[-1]
            stack.append((i, j))
        return result