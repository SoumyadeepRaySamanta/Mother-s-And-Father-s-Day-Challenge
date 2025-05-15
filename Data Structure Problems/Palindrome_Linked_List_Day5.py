# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # Find the middle of the linked list
        tortoise = hare = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
        
        # Step 2: Reverse the second half of the list
        prev = None
        while tortoise:
            next_node = tortoise.next
            tortoise.next = prev
            prev = tortoise
            tortoise = next_node
        
        # Step 3: Compare first half and reversed second half
        first_half, second_half = head, prev
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        return True
