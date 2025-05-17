class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create a set to store unique elements
        seen = set()
        
        # Traverse through each number in the list
        for num in nums:
            # If number is already in set, it's a duplicate
            if num in seen:
                return True
            # Otherwise, add it to the set
            seen.add(num)
        
        # If no duplicates found
        return False
