class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
     from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(arr: List[int], start: int, end: int) -> None:
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        n = len(nums)
        k %= n  # Handle k > n

        # Reverse first n - k elements
        reverse(nums, 0, n - k - 1)
        # Reverse last k elements
        reverse(nums, n - k, n - 1)
        # Reverse the entire array
        reverse(nums, 0, n - 1)


      