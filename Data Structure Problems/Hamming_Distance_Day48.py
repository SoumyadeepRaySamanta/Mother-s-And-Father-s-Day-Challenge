class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
        Algorithm:
        - XOR the two numbers: bits that are different will become 1.
        - Count the number of 1s in the result using bin().count('1').

        Time Complexity: O(1) (since integers are 32-bit max)
        Space Complexity: O(1)
        """

        return bin(x ^ y).count('1')
