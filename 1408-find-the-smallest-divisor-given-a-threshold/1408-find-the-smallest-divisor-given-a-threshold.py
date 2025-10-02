import math
def sumByD(nums,mid):
    n=len(nums) # size of array
    # Find the summation of division values
    total_sum=0
    for i in range(n):
        total_sum += math.ceil(nums[i]/mid)
    return total_sum

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n=len(nums)
        if n>threshold:
            return -1
        #calculate max
        maxi=float('-inf')
        for i in range(n):
            maxi=max(maxi,nums[i])
        # Apply binary search
        low=1
        high=maxi  #or high=max(nums)

        while low <= high:
            mid=(low+high) // 2
            if sumByD(nums,mid) <=threshold :
                high=mid-1
            else:
                low=mid+1    
        return low        #As low always have your ans