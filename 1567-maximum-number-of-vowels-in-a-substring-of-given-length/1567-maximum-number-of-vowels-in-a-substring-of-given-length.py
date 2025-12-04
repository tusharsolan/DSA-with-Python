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
            # p =s[exclude:include]

            # print("old window : ",p, ",cnt", cnt , ", maxi :", maxi )

            if s[include] in vowel :
                cnt+=1
            if s[exclude] in vowel:
                cnt-=1  
            include+=1
            exclude+=1 

            maxi=max(maxi,cnt)
            # print("new window : ",p, ",cnt", cnt , ", maxi :", maxi )



        return maxi     
            

       
# old window :  abc ,cnt 1 , maxi : 1
# new window :  abc ,cnt 1 , maxi : 1
# old window :  bci ,cnt 1 , maxi : 1
# new window :  bci ,cnt 2 , maxi : 2
# old window :  cii ,cnt 2 , maxi : 2
# new window :  cii ,cnt 3 , maxi : 3
# old window :  iii ,cnt 3 , maxi : 3
# new window :  iii ,cnt 2 , maxi : 3
# old window :  iid ,cnt 2 , maxi : 3
# new window :  iid ,cnt 2 , maxi : 3
# old window :  ide ,cnt 2 , maxi : 3
# new window :  ide ,cnt 1 , maxi : 3

        
        
        