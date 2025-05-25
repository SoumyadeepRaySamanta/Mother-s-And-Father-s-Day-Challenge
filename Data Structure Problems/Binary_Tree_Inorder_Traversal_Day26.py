class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def inorder(node: Optional[TreeNode]):
            if node:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)

        inorder(root)
        return result
