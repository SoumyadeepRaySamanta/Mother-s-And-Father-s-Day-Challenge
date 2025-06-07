# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Algorithm:
        - Use BST property: left < root < right.
        - Traverse the tree:
            - If val < root.val → go left
            - If val > root.val → go right
        - When reaching a None position (empty spot), insert the new node there.
        - Return the (possibly unchanged) root node.

        Time Complexity: O(h), where h = height of the tree
        Space Complexity: O(h) due to recursion stack
        """

        if not root:
            # Insert new node at correct leaf position
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root
