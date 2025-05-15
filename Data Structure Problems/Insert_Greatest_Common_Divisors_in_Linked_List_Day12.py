# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            # Calculate the GCD of current and next node values
            g = gcd(current.val, current.next.val)
            
            # Create a new node with GCD value
            new_node = ListNode(g)
            
            # Insert the new node between current and current.next
            new_node.next = current.next
            current.next = new_node
            
            # Move to the node after the inserted one
            current = new_node.next
        
        return head
