def findDays(weights,cap):
    days=1  # First day
    load=0
    n=len(weights) # size of array
    for i in range(n):
        if load + weights[i] > cap:
            days +=1 # move to next day
            load = weights[i] # load the weight
        else:
            # load the weight on the same day
            load += weights[i]
    return days            


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Find the maximum and the summation
        low= max(weights)
        high = sum(weights)

        while low<= high:
            mid = (low+high) // 2
            noOfDays = findDays(weights,mid)
            if noOfDays <= days:
                # Eliminate right half
                high = mid - 1
            else:
                # Eliminate left half
                low= mid + 1
        return low            
    
        