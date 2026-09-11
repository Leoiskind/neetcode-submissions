class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')': '(',
        '}': '{',
        ']': '['}
        for i in range(len(s)):
            if s[i] in closeToOpen:
                if stack and stack[-1] == closeToOpen[s[i]]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(s[i])
        if len(stack) == 0:
            return True
        else:
            return False
        