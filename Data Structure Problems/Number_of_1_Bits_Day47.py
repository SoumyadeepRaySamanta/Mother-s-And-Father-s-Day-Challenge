class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Algorithm:
        - Use Brian Kernighan's algorithm:
          repeatedly turn off the rightmost set bit until n becomes 0.
        - Each operation removes one '1' from n.
        - Count how many times this is done.

        Time Complexity: O(k), where k is the number of 1-bits in n
        Space Complexity: O(1)
        """

        count = 0
        while n:
            n &= n - 1  # Drop the lowest set bit
            count += 1
        return count
