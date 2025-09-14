from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lowerBound(nums: List[int], target: int) -> int:
            n = len(nums)
            low, high = 0, n - 1
            ans = n
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] >= target:
                    ans = mid
                    high = mid - 1  # look left
                else:
                    low = mid + 1   # look right
            return ans

        def upperBound(nums: List[int], target: int) -> int:
            n = len(nums)
            low, high = 0, n - 1
            ans = n
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > target:
                    ans = mid
                    high = mid - 1  # look left
                else:
                    low = mid + 1   # look right
            return ans

        n = len(nums)
        lb = lowerBound(nums, target)
        if lb == n or nums[lb] != target:
            return [-1, -1]
        return [lb, upperBound(nums, target) - 1]
