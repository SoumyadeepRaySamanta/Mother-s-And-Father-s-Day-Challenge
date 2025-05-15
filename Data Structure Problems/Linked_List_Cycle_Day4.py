# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Solved by Soumyadeep Ray Samanta on 03/05/2025
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = hare = head                  # Initialize two pointers, both starting at the head

        # Traverse the list
        while hare and hare.next:
            tortoise = tortoise.next            # Move tortoise by 1 step
            hare = hare.next.next               # Move hare by 2 steps

            # If these two pointers meet, a cycle exists
            if tortoise is hare:
                return True
        
        #If we reach here, hare reached the end => no cycle
        return False
