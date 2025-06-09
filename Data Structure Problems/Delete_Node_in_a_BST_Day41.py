# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Algorithm:
        - Traverse the tree using BST rules to find the node with value == key.
        - If found:
            Case 1: Node has no children → return None.
            Case 2: Node has one child → return that child.
            Case 3: Node has two children:
                - Find the inorder successor (min node in right subtree),
                - Replace node’s value with successor’s,
                - Recursively delete the successor.

        Time Complexity: O(h), where h = height of the tree
        Space Complexity: O(h) due to recursion
        """

        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node with only one or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Node with two children:
            # Find inorder successor (smallest in right subtree)
            min_larger_node = self.getMin(root.right)
            root.val = min_larger_node.val  # Copy successor's value
            # Delete the successor
            root.right = self.deleteNode(root.right, min_larger_node.val)

        return root

    def getMin(self, node: TreeNode) -> TreeNode:
        # Helper to find the leftmost (minimum) node
        while node.left:
            node = node.left
        return node
