class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        prefix=[0]*n
        suffix=[0]*n
        prefix[0]=height[0]
        for i in range(1,n):
            prefix[i]=max(height[i],prefix[i-1])
        suffix[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            suffix[i]=max(height[i], suffix[i + 1])   

        waterTrapped=0
        for i in range(n):
            waterTrapped += min(prefix[i],suffix[i]) - height[i]
        return waterTrapped        
