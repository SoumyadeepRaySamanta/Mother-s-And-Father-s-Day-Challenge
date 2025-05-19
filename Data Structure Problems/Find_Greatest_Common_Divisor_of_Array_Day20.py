class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # Step 1: Find the smallest and largest numbers in the list
        smallest = min(nums)
        largest = max(nums)

        # Step 2: Define a helper function to compute GCD using Euclidean algorithm
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        # Step 3: Return GCD of smallest and largest
        return gcd(smallest, largest)
