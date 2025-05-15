# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even  # Save the head of even list to attach at the end

        while even and even.next:
            odd.next = even.next  # Link odd to the next odd node
            odd = odd.next        # Move odd pointer
            even.next = odd.next  # Link even to the next even node
            even = even.next      # Move even pointer

        odd.next = even_head  # Attach even list after odd list
        return head
