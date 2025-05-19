class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # Step 1: Initialize an empty stack

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # Step 2a: Pop the top two operands from the stack
                b = stack.pop()
                a = stack.pop()

                # Step 2b: Apply the operator and push the result back
                if token == "+":
                    stack.append(a + b)  # Add
                elif token == "-":
                    stack.append(a - b)  # Subtract
                elif token == "*":
                    stack.append(a * b)  # Multiply
                elif token == "/":
                    # Integer division with truncation toward zero
                    stack.append(int(a / b))
            else:
                # Step 2c: If token is a number, push it to the stack
                stack.append(int(token))

        # Step 3: Final result will be the only element in the stack
        return stack[0]
