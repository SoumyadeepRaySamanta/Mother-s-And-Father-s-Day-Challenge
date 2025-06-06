class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Algorithm:
        - Use two pointers: one from the start (left), one from the end (right).
        - Move both pointers towards the center, skipping non-alphanumeric characters.
        - At each step, compare the lowercase of both characters.
        - If mismatch found, return False.
        - If pointers meet or cross with all matches, return True.

        Helper:
        - str.isalnum(): checks if a character is alphanumeric.

        Time Complexity: O(n)
        Space Complexity: O(1) (excluding input)
        """

        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer to next alphanumeric
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer to previous alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters ignoring case
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
