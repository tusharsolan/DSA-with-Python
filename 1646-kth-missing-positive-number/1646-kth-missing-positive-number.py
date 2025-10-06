class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            missing = arr[mid] - (mid + 1)  # number of missing numbers before arr[mid]

            if missing < k:
                low = mid + 1
            else:
                high = mid - 1

        return low + k
