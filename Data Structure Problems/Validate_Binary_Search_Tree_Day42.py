# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function that uses recursion and value bounds
        def helper(node, lower=float('-inf'), upper=float('inf')):
            # Base case: An empty node (leaf's child) is valid
            if not node:
                return True

            val = node.val

            # Check if current node's value violates the BST property
            # It must be strictly greater than the lower bound
            # and strictly less than the upper bound
            if val <= lower or val >= upper:
                return False

            # Recursively validate the right subtree
            # All nodes in the right subtree must be greater than current node
            if not helper(node.right, val, upper):
                return False

            # Recursively validate the left subtree
            # All nodes in the left subtree must be less than current node
            if not helper(node.left, lower, val):
                return False

            # If both subtrees are valid, return True
            return True

        # Start the recursion with the entire range of valid values
        return helper(root)
