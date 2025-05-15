class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        res = 0
        
        # Handle edge case of 0 or no change number (x == 0)
        if x == 0:
            return 0
        
        sign = 1 if x > 0 else -1
        x = abs(x)
        
        while x:
            digit = x % 10
            res = res * 10 + digit
            x //= 10
        
        # Handle overflow after processing
        res = res * sign
        return res if INT_MIN <= res <= INT_MAX else 0
