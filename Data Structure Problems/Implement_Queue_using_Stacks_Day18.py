class MyQueue:

    def __init__(self):
        # Stack used for pushing new elements (rear of the queue)
        self.stack_in = []
        # Stack used for popping/peeking elements from front of queue
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        Always push onto stack_in.
        """
        self.stack_in.append(x)

    def pop(self) -> int:
        """
        Removes the element from the front of queue and returns it.
        If stack_out is empty, move all elements from stack_in to stack_out
        to reverse their order (to simulate FIFO).
        """
        self._transfer()
        return self.stack_out.pop()

    def peek(self) -> int:
        """
        Get the front element.
        Same logic as pop, but return the top without removing it.
        """
        self._transfer()
        return self.stack_out[-1]

    def empty(self) -> bool:
        """
        Return whether the queue is empty.
        It is empty only if both stacks are empty.
        """
        return not self.stack_in and not self.stack_out
    
    def _transfer(self):
        """
        Helper method:
        Move elements from stack_in to stack_out if stack_out is empty.
        This happens only when stack_out is empty and we need to pop/peek.
        Ensures amortized O(1) time.
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
