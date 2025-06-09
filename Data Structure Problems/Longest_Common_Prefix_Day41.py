class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Algorithm:
        - If the list is empty, return "".
        - Take the first string as reference.
        - For each character position in the first string:
            - Check if all strings have the same character at that position.
            - If not, return the prefix up to that point.
        - If loop finishes, the entire first string is the prefix.

        Time Complexity: O(n * m), where:
            n = number of strings
            m = length of the shortest string
        Space Complexity: O(1)
        """

        if not strs:
            return ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]

        return strs[0]
