# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        total = 0
        if root.left:
            # Check if it's a left leaf
            if not root.left.left and not root.left.right:
                total += root.left.val
        # Recur on left and right subtrees
        return total + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
