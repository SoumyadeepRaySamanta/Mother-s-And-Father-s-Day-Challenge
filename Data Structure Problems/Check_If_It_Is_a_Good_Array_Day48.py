class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        """
        Algorithm:
        - If GCD of all elements in nums is 1 → it's a good array.
        - Use reduce to apply gcd across the list.

        Why?
        - Bézout's Identity: ax + by = d (d = gcd(a, b))
        - So if gcd(nums) = 1 → 1 can be expressed using nums.

        Time Complexity: O(n * logM), where M = max(nums)
        Space Complexity: O(1)
        """

        return reduce(gcd, nums) == 1
