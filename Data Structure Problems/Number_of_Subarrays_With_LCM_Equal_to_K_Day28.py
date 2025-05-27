class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        def lcm(a, b):
            return a * b // gcd(a, b)

        count = 0
        n = len(nums)

        for i in range(n):
            current = nums[i]
            if k % current != 0:
                continue
            if current == k:
                count += 1

            for j in range(i + 1, n):
                if nums[j] > k or k % nums[j] != 0:
                    break  # nums[j] can't help reach LCM = k
                current = lcm(current, nums[j])
                if current > k:
                    break
                if current == k:
                    count += 1

        return count
