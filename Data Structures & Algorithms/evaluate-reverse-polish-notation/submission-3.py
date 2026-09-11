class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = set(['+', '-', '*', '/'])
        for i in range(len(tokens)):
            if tokens[i] in operands:
                if tokens[i]=='+':
                    total = stack.pop(-1) + stack.pop(-1)
                    stack.append(total)
                elif tokens[i]=='-':
                    total = -stack.pop(-1) + stack.pop(-1)
                    stack.append(total)
                elif tokens[i]=='*':
                    total = stack.pop(-1) * stack.pop(-1)
                    stack.append(total)
                elif tokens[i]=='/':
                    denom = stack.pop(-1)
                    num = stack.pop(-1)
                    stack.append(int(num/denom))
            else:
                stack.append(int(tokens[i]))
        return stack[-1]
