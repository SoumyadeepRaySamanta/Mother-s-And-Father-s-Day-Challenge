class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()

        # First pass to identify unmatched ')' and store indexes of unmatched '('
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)

        # Add unmatched '(' indexes to removal set
        to_remove.update(stack)

        # Build result string excluding characters at to_remove positions
        result = []
        for i, char in enumerate(s):
            if i not in to_remove:
                result.append(char)

        return ''.join(result)
