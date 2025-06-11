# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Algorithm:
        - Inorder traversal of BST yields sorted elements.
        - Perform an inorder traversal and keep a counter.
        - When the counter reaches k, return the current node's value.

        Time Complexity: O(h + k) in the average case,
                         O(n) in the worst case (unbalanced tree)
        Space Complexity: O(h) for recursion stack
        """

        self.count = 0
        self.result = None

        def inorder(node):
            if not node or self.result is not None:
                return
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.result
