class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                num=stack.pop()
                stack[-1] += num
            elif tokens[i] == "-":
                num=stack.pop()
                stack[-1] -= num
            elif tokens[i] == "*":
                num=stack.pop()
                stack[-1] *= num
            elif tokens[i] == "/":
                num=stack.pop()
                stack[-1] = int(stack[-1] / num)
            else:
                stack.append(int(tokens[i]))
        return stack.pop()
            