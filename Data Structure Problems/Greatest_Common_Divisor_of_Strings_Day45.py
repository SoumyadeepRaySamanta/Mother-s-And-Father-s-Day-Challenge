class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Algorithm:
        - If str1 + str2 != str2 + str1, there's no common divisor → return ""
        - Otherwise, the GCD string is str1[:gcd(len(str1), len(str2))]
        - We use math.gcd to compute the length of the largest string that can divide both.

        Time Complexity: O(n + m), where n and m are the lengths of str1 and str2
        Space Complexity: O(1)
        """
        from math import gcd

        # Check if concatenation order matters
        if str1 + str2 != str2 + str1:
            return ""

        # Return substring of length = GCD of their lengths
        return str1[:gcd(len(str1), len(str2))]
