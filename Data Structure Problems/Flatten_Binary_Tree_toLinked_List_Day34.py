# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Helper function to perform flattening using recursion
        def flatten_tree(node):
            if not node:
                return None  # Base case: if the node is null, nothing to flatten
            
            # Recursively flatten the left subtree
            left_tail = flatten_tree(node.left)

            # Recursively flatten the right subtree
            right_tail = flatten_tree(node.right)

            # If the node has a left subtree, we need to insert it
            # between the current node and the right subtree
            if node.left:
                # Save the current right subtree
                temp_right = node.right

                # Move the left subtree to the right
                node.right = node.left
                node.left = None  # Set the left child to None

                # Find the tail of the new right subtree (former left subtree)
                if left_tail:
                    left_tail.right = temp_right  # Connect the tail to the original right subtree

            # Return the rightmost node after flattening
            # This will be used by the parent node to connect correctly
            return right_tail or left_tail or node  # Return the deepest node

        # Start flattening from the root
        flatten_tree(root)
