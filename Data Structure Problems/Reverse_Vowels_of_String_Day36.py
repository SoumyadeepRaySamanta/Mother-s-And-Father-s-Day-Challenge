class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Algorithm:
        - Use two pointers: one from the start (left), one from the end (right).
        - Move both pointers until they point to vowels.
        - Swap the vowels, and move the pointers inward.
        - Continue until left >= right.

        Why this works:
        - We're only interested in vowels: a, e, i, o, u (case-insensitive).
        - By only swapping vowels, we preserve the positions of all non-vowels.

        Time Complexity: O(n)
        Space Complexity: O(n) if string is converted to list (Python strings are immutable)
        """

        vowels = set('aeiouAEIOU')  # Set for quick lookup
        s = list(s)  # Convert string to list for in-place modification
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer until it points to a vowel
            while left < right and s[left] not in vowels:
                left += 1

            # Move right pointer until it points to a vowel
            while left < right and s[right] not in vowels:
                right -= 1

            # Swap the vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)  # Convert list back to string
