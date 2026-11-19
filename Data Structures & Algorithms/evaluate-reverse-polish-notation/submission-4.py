class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        operations = {'+', '-', '*', '/'}

        for token in tokens:
            if token in operations:
            
                right = int(stack.pop())
                left = int(stack.pop())

                if token == '+':
                    res = left + right
                elif token == '-':
                    res = left - right
                elif token == '*':
                    res = left * right
                else:
                    if left < 0 or right < 0:
                        res = int(left / right)
                    else:
                        res = left // right
                
                stack.append(res)


            else:
                stack.append(token)

        if stack:
            res = int(stack.pop())

        return res
        