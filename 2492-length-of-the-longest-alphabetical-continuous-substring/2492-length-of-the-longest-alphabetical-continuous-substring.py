class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        n=len(s)
        
        cnt=1
        maxi=1
        
        for i in range(n-1):
            if ord(s[i+1]) - ord(s[i]) == 1:
                cnt+=1
            else:
                cnt=1  
            #print("outside loop", maxi, cnt)
            maxi=max(cnt,maxi)        

                
        return maxi      



        