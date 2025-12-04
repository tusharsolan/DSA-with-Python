class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n=len(s)
        vowel="aeiou"
        cnt=0
        #step-1 preprocess for first k window size
        for i in range(k):
            if s[i] in vowel:
                cnt+=1

        maxi=cnt  

        include=k
        exclude=0
        #step-2 move window till k reaches n
        while include<n:
            if s[include] in vowel :
                cnt+=1
            if s[exclude] in vowel:
                cnt-=1  
            include+=1
            exclude+=1 

            maxi=max(maxi,cnt)

        return maxi     
            

             

        
        
        