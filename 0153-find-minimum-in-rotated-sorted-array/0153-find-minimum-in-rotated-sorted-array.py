import sys
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        low=0
        high=n-1
        ans=sys.maxsize
        while low<=high:
            mid=(low+high) // 2
            if nums[low]<=nums[high]:
                ans=min(ans,nums[low])

            if nums[low]<=nums[mid]:
                ans= min(ans,nums[low])
                low=mid+1
            else:
                ans=min(ans,nums[mid])
                high=mid-1
        return ans            