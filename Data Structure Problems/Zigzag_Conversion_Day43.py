class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Algorithm:
        - If numRows == 1 or greater than len(s), return s (no zigzag possible).
        - Create an array `rows` of empty strings, one for each row.
        - Traverse through the string `s`:
            - Append each character to the correct row.
            - Use a direction flag to move up/down through rows (like zigzag).
        - Finally, join all rows to form the result.

        Time Complexity: O(n), where n = len(s)
        Space Complexity: O(n)
        """

        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        curr_row = 0
        going_down = False

        for char in s:
            rows[curr_row] += char
            # Change direction if at top or bottom
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
            # Move up or down
            curr_row += 1 if going_down else -1

        return ''.join(rows)
