class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        
        # Expected sum of numbers from 0 to n
        expected_sum = n * (n + 1) // 2

        # Actual sum of elements in the array
        actual_sum = sum(nums)

        # The missing number is the difference
        return expected_sum - actual_sum