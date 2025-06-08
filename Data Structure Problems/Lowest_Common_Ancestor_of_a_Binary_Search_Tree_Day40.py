# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Algorithm (Using BST properties):
        - Start from the root node.
        - If both p and q values are less than root → LCA is in the left subtree.
        - If both p and q values are greater than root → LCA is in the right subtree.
        - If p <= root <= q or q <= root <= p → root is the LCA.

        Time Complexity: O(h), where h = height of the tree
        Space Complexity: O(1) (iterative version)
        """

        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left  # Move left
            elif p.val > root.val and q.val > root.val:
                root = root.right  # Move right
            else:
                return root  # This is the split point → LCA
