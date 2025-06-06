# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Algorithm:
        - Binary Search Tree property:
            Left subtree contains values < root.val
            Right subtree contains values > root.val
        - Start from root:
            - If root is None → return None
            - If val == root.val → node found, return root
            - If val < root.val → search in left subtree
            - If val > root.val → search in right subtree

        Time Complexity: O(h), where h = height of the tree
        Space Complexity: O(h) for recursion stack (O(log n) for balanced, O(n) worst case)
        """

        if not root:
            return None

        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
