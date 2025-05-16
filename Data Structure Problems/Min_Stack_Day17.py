class MinStack:

    def __init__(self):
        # Initialize two stacks:
        # 1. stack: to store all pushed values
        # 2. min_stack: to store the minimum value at each level of the main stack
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # Push the value onto the main stack
        self.stack.append(val)

        # If min_stack is empty or current val is smaller than or equal to
        # the current minimum, push val onto min_stack
        # Else, repeat the current minimum (top of min_stack)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

        # This ensures min_stack is always in sync with stack,
        # and top of min_stack is the current minimum


    def pop(self) -> None:
        # Pop from both stack and min_stack to remove the top element
        self.stack.pop()
        self.min_stack.pop()
        # This keeps both stacks aligned and maintains correct minimum

    def top(self) -> int:
        # Return the top of the main stack
        return self.stack[-1]
        
    def getMin(self) -> int:
        # Return the top of the min_stack, which is the current minimum
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
