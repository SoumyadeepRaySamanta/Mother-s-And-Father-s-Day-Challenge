class Solution:
    def countPrimes(self, n: int) -> int:
        """
        Algorithm: Sieve of Eratosthenes
        - Create a boolean array `is_prime` of size n, initialized as True.
        - Set is_prime[0] and is_prime[1] to False (0 and 1 are not primes).
        - For every number i from 2 to sqrt(n):
            - If i is prime, mark all multiples of i as not prime.
        - Count all True values in is_prime from index 2 to n-1.

        Time Complexity: O(n log log n)
        Space Complexity: O(n)
        """

        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return sum(is_prime)
