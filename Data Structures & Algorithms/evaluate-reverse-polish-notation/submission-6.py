class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        output = 0
        operations = {'+', '-', '*', '/'}
        stack = []

        for token in tokens:
            if token in operations:
                right = int(stack.pop())
                left = int(stack.pop())

                if token == '+':
                    output = left + right
                elif token == '-':
                    output = left - right
                elif token == '*':
                    output = left * right
                else:
                    if right < 0 or left < 0:
                        output = left / right
                    else:
                        output = left // right
                stack.append(output)
            else:
                stack.append(token)

        if stack:
            output = int(stack.pop())

        return output
        