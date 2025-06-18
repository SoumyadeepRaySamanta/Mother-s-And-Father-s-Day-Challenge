class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        """
        Algorithm:
        - If length is 1 → cannot break the palindrome → return ""
        - For the first half of the string:
            - Change the first non-'a' character to 'a' to make it lexicographically smaller.
        - If all characters in first half are 'a', change the last character to 'b'.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        if len(palindrome) == 1:
            return ""

        chars = list(palindrome)

        for i in range(len(palindrome) // 2):
            if chars[i] != 'a':
                chars[i] = 'a'
                return "".join(chars)

        chars[-1] = 'b'
        return "".join(chars)
