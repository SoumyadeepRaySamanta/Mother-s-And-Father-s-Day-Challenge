class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        Algorithm:
        - Use a stack to keep track of characters.
        - For each character in the string:
            - If the stack is not empty and the top is the same as current char:
                → pop (remove the duplicate pair)
            - Else:
                → push the character onto the stack.
        - After processing all characters, join the stack into the result string.

        Time Complexity: O(n)
        Space Complexity: O(n) (stack space)
        """

        stack = []

        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()  # Remove the duplicate
            else:
                stack.append(ch)  # Add new character

        return ''.join(stack)
