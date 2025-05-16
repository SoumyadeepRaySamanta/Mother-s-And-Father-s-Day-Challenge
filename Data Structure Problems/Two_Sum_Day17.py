class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hash map to store value: index pairs
        num_to_index = {}

        # Traverse the array
        for i, num in enumerate(nums):
            # Calculate the complement that we need to find
            complement = target - num

            # Check if the complement is already in the map
            if complement in num_to_index:
                # If found, return the indices of complement and current number
                return [num_to_index[complement], i]

            # Otherwise, store the current number and its index in the map
            num_to_index[num] = i

        # The problem guarantees exactly one solution, so no need for a default return
