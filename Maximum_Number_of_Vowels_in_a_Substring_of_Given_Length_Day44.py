class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        Algorithm:
        - Use a sliding window of size k.
        - Count vowels in the first window.
        - Slide the window through the string:
            - Subtract the leftmost character if it's a vowel.
            - Add the new character on the right if it's a vowel.
        - Keep track of the maximum vowel count seen.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        vowels = set('aeiou')
        count = 0
        max_count = 0

        # Count vowels in the first window of size k
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count

        # Slide the window
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            max_count = max(max_count, count)

        return max_count
