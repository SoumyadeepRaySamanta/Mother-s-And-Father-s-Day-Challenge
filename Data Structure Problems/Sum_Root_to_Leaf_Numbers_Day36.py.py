# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Algorithm:
        - We use Depth-First Search (DFS) to explore all paths from root to leaf.
        - While traversing, we build the current number by multiplying the previous value by 10 and adding the current node’s digit.
        - When we reach a leaf node, we add the complete number to the result.
        
        Steps:
        1. Initialize a helper function dfs(node, current_number).
        2. For each node:
           - Update the current number.
           - If it’s a leaf node, return the number.
           - Else, recurse on left and right child.
        3. Sum up the results from both subtrees.
        """

        def dfs(node, current_number):
            if not node:
                return 0

            # Update the current number
            current_number = current_number * 10 + node.val

            # If it's a leaf node, return the full number
            if not node.left and not node.right:
                return current_number

            # Otherwise, sum the numbers from left and right subtrees
            left_sum = dfs(node.left, current_number)
            right_sum = dfs(node.right, current_number)

            return left_sum + right_sum

        return dfs(root, 0)
