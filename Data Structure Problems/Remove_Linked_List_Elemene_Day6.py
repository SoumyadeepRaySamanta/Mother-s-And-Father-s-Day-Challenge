# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode(0)                              # Creating a temporary node before the head
        temp.next = head                                # Point temporary's next to the current head
        current = temp                                  # Start from the temporary node

        while current.next:                             # Traverse the list until the end
            if current.next.val == val:
                current.next = current.next.next        # Skip the node with the va;ue
            else:
                current = current.next                  # Move to the next node
        
        return temp.next                                # Return the new node
