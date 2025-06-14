class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        """
        Algorithm:
        - For each number from left to right:
            - Count the number of set bits (1s) in its binary representation.
            - Check if the count is a prime number.
        - Return the total count of such numbers.

        Optimization:
        - Maximum number of bits for numbers ≤ 10^6 is 20.
        - So we can predefine the set of primes ≤ 20.

        Time Complexity: O(n * log m), where:
            n = right - left + 1
            m = maximum number (to count set bits)
        Space Complexity: O(1)
        """

        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x**0.5)+1):
                if x % i == 0:
                    return False
            return True

        count = 0
        for num in range(left, right + 1):
            set_bits = bin(num).count('1')  # count of '1's in binary
            if is_prime(set_bits):
                count += 1
        return count
