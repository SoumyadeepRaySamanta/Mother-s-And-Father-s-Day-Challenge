class Solution:
    def countSegments(self, s: str) -> int:
        """
        Algorithm:
        - We manually count the number of segments (words) in the string.
        - A segment starts when:
            - The current character is NOT a space
            - AND either it's the first character or the previous character is a space
        - This way, we only count the beginning of each segment once.

        Example:
        Input: "Hello, my name is John"
        Output: 5

        Time Complexity: O(n) where n = length of string
        Space Complexity: O(1)
        """

        count = 0
        n = len(s)

        for i in range(n):
            # If current char is not space and either it's the first char
            # or the previous char is a space, it's the start of a segment
            if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
                count += 1

        return count
