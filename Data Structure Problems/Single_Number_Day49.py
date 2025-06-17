class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Algorithm:
        - Use XOR to cancel out pairs:
            - a ^ a = 0
            - a ^ 0 = a
        - So all numbers appearing twice cancel each other out, leaving the single one.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        result = 0
        for num in nums:
            result ^= num
        return result
