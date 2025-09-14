from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_occurrence(nums, target):
            start, end = 0, len(nums) - 1
            res = -1
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    res = mid
                    end = mid - 1   # move left to find first occurrence
                elif target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            return res

        def last_occurrence(nums, target):
            start, end = 0, len(nums) - 1
            res = -1
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    res = mid
                    start = mid + 1   # move right to find last occurrence
                elif target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            return res

        first = first_occurrence(nums, target)
        last = last_occurrence(nums, target)
        return [first, last]
