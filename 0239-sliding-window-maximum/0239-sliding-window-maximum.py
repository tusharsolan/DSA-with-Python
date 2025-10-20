class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []

        for i in range(len(nums)):
        # Remove elements out of the current window
            if dq and dq[0] == i - k:
                dq.popleft()

            # Remove smaller elements (theyâre not useful)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Record the max for the current window
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans