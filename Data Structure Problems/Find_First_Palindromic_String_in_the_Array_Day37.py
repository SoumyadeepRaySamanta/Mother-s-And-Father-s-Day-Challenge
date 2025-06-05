class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        """
        Algorithm:
        - Iterate over each word in the list.
        - For each word, check if it's a palindrome.
          (i.e., it reads the same forward and backward)
        - If found, return that word immediately.
        - If no palindrome is found after the loop, return an empty string.

        Palindrome Check:
        - We compare the string with its reverse: word == word[::-1]

        Time Complexity: O(n * m), where:
          n = number of words,
          m = average length of each word.
        Space Complexity: O(1) (excluding input)
        """

        for word in words:
            if word == word[::-1]:  # Palindrome check
                return word

        return ""  # No palindrome found
