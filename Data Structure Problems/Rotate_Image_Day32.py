class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Algorithm:
        We rotate the matrix 90 degrees clockwise in two steps:

        Step 1: Transpose the matrix.
        - Transposing means converting rows into columns.
        - We do this by swapping matrix[i][j] with matrix[j][i] for all i < j.
        - After transposing, the top-left to bottom-right diagonal remains the same.

        Step 2: Reverse each row manually (no built-in functions).
        - To get the rotated matrix, we reverse every row (i.e., swap the first and last elements, then move inward).

        Example:
        Input:
        [
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
        ]

        Step 1 (Transpose):
        [
          [1, 4, 7],
          [2, 5, 8],
          [3, 6, 9]
        ]

        Step 2 (Reverse each row):
        [
          [7, 4, 1],
          [8, 5, 2],
          [9, 6, 3]
        ]
        """

        n = len(matrix)

        # Step 1: Transpose the matrix manually
        for i in range(n):
            for j in range(i + 1, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        # Step 2: Reverse each row manually
        for i in range(n):
            left = 0
            right = n - 1
            while left < right:
                temp = matrix[i][left]
                matrix[i][left] = matrix[i][right]
                matrix[i][right] = temp
                left += 1
                right -= 1
        
