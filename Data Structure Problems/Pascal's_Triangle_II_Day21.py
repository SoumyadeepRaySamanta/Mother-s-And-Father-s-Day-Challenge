class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Initialize the row with the first element as 1
        row = [1]

        # Use the formula to build each value of the row
        # row[i] = row[i - 1] * (rowIndex - i + 1) // i
        for i in range(1, rowIndex + 1):
            value = row[i - 1] * (rowIndex - i + 1) // i
            row.append(value)

        return row
