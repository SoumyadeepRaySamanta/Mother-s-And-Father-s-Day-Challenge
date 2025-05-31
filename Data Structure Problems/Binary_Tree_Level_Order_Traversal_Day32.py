# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Algorithm:
        # This problem is best solved using Breadth-First Search (BFS),
        # which processes nodes level-by-level.
        #
        # 1. Use a queue (FIFO) to keep track of nodes at each level.
        # 2. Start by enqueuing the root node.
        # 3. For each level:
        #    - Determine the number of nodes in that level (queue length).
        #    - Dequeue each node, add its value to a temporary list.
        #    - Enqueue its children (left and right) if they exist.
        # 4. After processing the level, append the temporary list to the result.

        if not root:
            return []  # If the tree is empty, return an empty list.

        result = []               # To store the final level order traversal.
        queue = deque([root])     # Initialize the queue with the root node.

        while queue:
            level_size = len(queue)  # Number of nodes at the current level.
            level = []               # List to store values of the current level.

            for _ in range(level_size):
                node = queue.popleft()   # Dequeue the node from the front.
                level.append(node.val)  # Add its value to the level list.

                # Enqueue left and right children if they exist.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)  # Add this level's values to the result.

        return result
