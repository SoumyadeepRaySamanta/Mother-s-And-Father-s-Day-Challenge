# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Algorithm (Recursive DFS approach):
        - Base case: If root is None, or root is either p or q, return root.
        - Recursively search the left and right subtrees for p and q.
        - If both left and right recursive calls return non-null:
            → This means p and q are found in **different** subtrees,
              so the current root is their **lowest common ancestor**.
        - If only one side returns a node (non-null):
            → It means both p and q are located in that subtree,
              so return that node upwards.
        - If neither returns anything (both None), return None.

        Time Complexity: O(n), where n = number of nodes (we visit each node once).
        Space Complexity: O(h), where h = height of the tree (due to recursion stack).
        """

        # Base case
        if root is None or root == p or root == q:
            return root

        # Search left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides return a result, current node is the LCA
        if left and right:
            return root

        # Else, return the side that is non-null
        return left if left else right
