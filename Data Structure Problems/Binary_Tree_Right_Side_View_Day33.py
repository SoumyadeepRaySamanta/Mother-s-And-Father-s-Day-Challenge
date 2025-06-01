# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Algorithm:
        - This problem is solved using **Breadth-First Search (BFS)** level-order traversal.
        - We traverse the tree level by level and for each level, we take the **last node**.
        - That last node is what would be visible from the right side.

        Steps:
        1. If the tree is empty, return an empty list.
        2. Use a queue (FIFO) to do level-order traversal.
        3. At each level:
           - Get the number of nodes at the current level.
           - Traverse all nodes at this level and push their children into the queue.
           - Keep track of the last node's value in the level, and add it to the result.
        4. Return the result list after the traversal is complete.
        """

        if not root:
            return []

        result = []
        queue = deque([root])  # Initialize queue with the root node

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                # If it's the last node in the level, add its value to result
                if i == level_size - 1:
                    result.append(node.val)

                # Add left and right children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
