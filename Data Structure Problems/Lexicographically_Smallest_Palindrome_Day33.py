class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        """
        Algorithm:
        - A palindrome reads the same from both ends.
        - We iterate from both ends towards the center (two pointers).
        - For each pair of characters s[i] and s[n - 1 - i]:
            - If they are not equal:
                - Change the character that is lexicographically larger to match the smaller one.
            - If they are already equal, do nothing.
        - This guarantees both:
            - It becomes a palindrome.
            - It is the smallest lexicographically possible.

        Example:
        Input: "egcfe"
        After comparing and updating:
        -> compare 'e' and 'e' → same, no change
        -> compare 'g' and 'f' → change 'g' to 'f' → "efcfe"
        Final palindrome: "efcfe"
        """

        s = list(s)  # Convert to list to allow modification
        n = len(s)

        for i in range(n // 2):
            j = n - 1 - i  # Index from the right end
            if s[i] != s[j]:
                # Choose the smaller character to ensure smallest lexicographical result
                smaller_char = min(s[i], s[j])
                s[i] = s[j] = smaller_char

        return ''.join(s)  # Convert list back to string
