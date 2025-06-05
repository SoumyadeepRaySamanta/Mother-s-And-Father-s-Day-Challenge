# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Algorithm:
        - Perform a level-order traversal (BFS) using a queue.
        - For each level, use a temporary list to store the current level’s values.
        - If the level is even (0-indexed), append left to right.
        - If the level is odd, append right to left (i.e., reverse before appending).
        - After processing all nodes in the level, append the list to the result.
        
        Time Complexity: O(n) — every node is visited once.
        Space Complexity: O(n) — for the result list and queue.
        """

        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True  # Toggle direction at each level

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()

                # Append based on current direction
                if left_to_right:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)  # Insert at beginning for reverse order

                # Enqueue children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)
            left_to_right = not left_to_right  # Toggle direction for next level

        return result
