# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base Case: If the tree is empty, the depth is 0
        if not root:
            return 0
        
        # Recursive Case:
        # 1. Recursively compute the depth of the left subtree
        # 2. Recursively compute the depth of the right subtree
        # 3. The depth of the current node is 1 (for itself) + max of left and right subtree depths
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
