class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        Elements_sum = sum(nums)
        return total - Elements_sum
