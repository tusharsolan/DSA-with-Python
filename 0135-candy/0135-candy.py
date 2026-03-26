class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Get number of children
        n = len(ratings)
        sum = 1 # first child gets 1 candy

        # Start from second child
        i = 1

        while i < n:

            # Skip equal ratings
            if ratings[i] == ratings[i - 1]:
                sum += 1   # give 1 candy
                i += 1
                continue

            # Initialize increasing slope counter
            peak = 1

            # Traverse strictly increasing ratings
            while i < n and ratings[i] > ratings[i - 1]:
                peak += 1
                sum += peak
                i += 1

            # Initialize decreasing slope counter
            down = 1

            # Traverse strictly decreasing ratings
            while i < n and ratings[i] < ratings[i - 1]:
                sum += down
                down += 1
                i += 1
            if down > peak:
                sum += down - peak
        # Return total sum required
        return sum
        