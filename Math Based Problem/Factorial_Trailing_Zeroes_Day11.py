class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0  # Initialize a counter for the number of trailing zeroes
        
        # Keep dividing n by 5 to count multiples of 5, 25, 125, etc.
        while n > 0:
            n //= 5       # Reduce n by dividing it by 5
            count += n    # Add the number of factors of 5 in current n
        
        return count  # Return the total count of trailing zeroes
