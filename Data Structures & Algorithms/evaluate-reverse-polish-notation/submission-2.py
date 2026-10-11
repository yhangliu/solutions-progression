class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-*/"
        for token in tokens:
            if token in operators:
                if token == '+':
                    element_1 = stack.pop()
                    element_2 = stack.pop()
                    result = element_1 + element_2
                    stack.append(result)
                elif token == '*':
                    element_1 = stack.pop()
                    element_2 = stack.pop()
                    result = element_1 * element_2
                    stack.append(result)
                elif token == '-':
                    element_1 = stack.pop()
                    element_2 = stack.pop()
                    result = element_2 - element_1
                    stack.append(result)
                elif token == '/':
                    element_1 = stack.pop()
                    element_2 = stack.pop()
                    result = int(element_2/element_1)
                    stack.append(result)
                print(stack[-1])
            else:
                stack.append(int(token))
        if stack:
            return stack.pop()