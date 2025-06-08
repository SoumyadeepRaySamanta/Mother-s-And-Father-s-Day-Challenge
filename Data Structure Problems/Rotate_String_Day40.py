class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        Algorithm:
        - If s and goal are not of the same length, return False.
        - If goal is a substring of (s + s), then some rotation of s gives goal.
        - Why? Because all possible rotations of s are present in s + s.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        if len(s) != len(goal):
            return False

        return goal in (s + s)
