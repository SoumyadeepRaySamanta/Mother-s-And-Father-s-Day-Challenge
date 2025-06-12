# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        Algorithm:
        - Use slow & fast pointer to find the middle of the list (middle becomes the root).
        - Recursively:
            - Left part of the list → builds left subtree.
            - Right part of the list → builds right subtree.
        - Disconnect left part by setting prev.next = None.

        Time Complexity: O(n log n)
        Space Complexity: O(log n) due to recursion
        """

        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        # Find the middle node (slow will point to mid)
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Disconnect the left half
        if prev:
            prev.next = None

        # Create root with mid value
        root = TreeNode(slow.val)

        # Recursively build left and right subtrees
        root.left = self.sortedListToBST(head if slow != head else None)
        root.right = self.sortedListToBST(slow.next)

        return root
