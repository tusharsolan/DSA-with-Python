def Possible(bloomDay,mid,m,k):
        n=len(bloomDay)# size of the array
        cnt=0
        noOfB=0
        # count the number of bouquets
        for i in range(n):
            if bloomDay[i]<= mid:
                cnt+=1
            else:
                noOfB+=cnt//k
                cnt=0
        noOfB+=cnt//k
        return noOfB >=m

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        value=m*k
        n=len(bloomDay)# size of the array
        if value>n:
            return -1  # impossible case
        # find maximum and minimum    
        mini=float('inf')
        maxi=float('-inf')
        for i in range(n):
            mini=min(mini,bloomDay[i])
            maxi=max(maxi,bloomDay[i])

        
    # apply binary search
        low=mini
        high=maxi

        while low<=high:
            mid=(low+high)//2
            if Possible(bloomDay,mid,m,k):
                high=mid-1
            else:
                low=mid+1
        return low #As low will bw having the solution                  

    