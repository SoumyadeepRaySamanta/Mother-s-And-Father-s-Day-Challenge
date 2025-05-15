# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None  # If list has 0 or 1 node, return None

        tortoise = head
        hare = head
        prev = None

        # Use fast and slow pointer to find middle
        while hare and hare.next:
            prev = tortoise
            tortoise = tortoise.next
            hare = hare.next.next

        # Delete the middle node
        prev.next = tortoise.next

        return head
