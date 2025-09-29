import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)  # No need for custom FindMax

        while low <= high:
            mid = (low + high) // 2
            totalh = self.calculateTotalHours(piles, mid)

            if totalh > h:
                low = mid + 1  # Need to eat faster
            else:
                high = mid - 1  # Try a slower speed

        return low

    def calculateTotalHours(self, piles: List[int], speed: int) -> int:
        totalh = 0
        for pile in piles:
            totalh += math.ceil(pile / speed)
        return totalh
