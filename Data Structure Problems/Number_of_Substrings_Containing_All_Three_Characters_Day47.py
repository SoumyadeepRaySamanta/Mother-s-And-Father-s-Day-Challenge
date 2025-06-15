class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        Algorithm:
        - Use sliding window with two pointers (left and right).
        - Keep track of the count of 'a', 'b', 'c' in the current window.
        - For each valid window (contains all 3 characters), all substrings
          ending at right and starting from [left, left+1, ..., right] are valid.
        - So we add (len(s) - right) to result when valid.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        from collections import defaultdict

        count = defaultdict(int)
        res = 0
        left = 0

        for right in range(len(s)):
            count[s[right]] += 1

            # Shrink from the left while window contains all three characters
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                # Add all substrings starting at left and ending at right
                res += len(s) - right
                count[s[left]] -= 1
                left += 1

        return res
