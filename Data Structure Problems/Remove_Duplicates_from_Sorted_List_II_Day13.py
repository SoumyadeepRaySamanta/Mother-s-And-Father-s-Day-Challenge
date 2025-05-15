# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0, head)
        prev = temp

        while head:
            # Check if current node is a start of duplicates
            if head.next and head.val == head.next.val:
                # Skip all nodes with the same value
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next  # Remove all duplicates
            else:
                prev = prev.next
            head = head.next
        
        return temp.next
