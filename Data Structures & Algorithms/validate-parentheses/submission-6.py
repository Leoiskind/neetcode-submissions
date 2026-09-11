class Solution:
    def isValid(self, s: str) -> bool:
        brackets = set(['(', '{', '['])
        stack = []
        for i in range(len(s)):
            if s[i]==')':
                if stack and stack[-1] == '(':
                    stack.pop(-1)
                else:
                    return False
            elif s[i]=='}':
                if stack and stack[-1] == '{':
                    stack.pop(-1)
                else:
                    return False
            elif s[i]==']':
                if stack and stack[-1] == '[':
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(s[i])
        if len(stack) == 0:
            return True
        else:
            return False
        