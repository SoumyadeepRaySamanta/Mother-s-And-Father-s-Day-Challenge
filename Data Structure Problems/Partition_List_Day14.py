# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create two dummy nodes to separate the two partitions
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        # These will be the pointers that will help us build the two partitions
        less = less_head
        greater = greater_head
        
        # Traverse the original list
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next
        
        # Terminate the greater list to avoid cycle
        greater.next = None
        
        # Connect the two partitions
        less.next = greater_head.next
        
        return less_head.next
