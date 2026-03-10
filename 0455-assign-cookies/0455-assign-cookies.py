class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l=0
        r=0
        n=len(g)
        m=len(s)
        while l<m and r<n:
            if g[r] <= s[l]:
                r+=1
            l+=1 
        return r               