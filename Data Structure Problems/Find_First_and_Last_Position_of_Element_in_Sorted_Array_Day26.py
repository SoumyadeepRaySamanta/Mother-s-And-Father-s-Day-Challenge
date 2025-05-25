class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left():
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    if nums[mid] == target:
                        index = mid
            return index

        def find_right():
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                    if nums[mid] == target:
                        index = mid
            return index

        return [find_left(), find_right()]
