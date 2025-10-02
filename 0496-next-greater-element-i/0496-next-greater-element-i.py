class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums2)
        nge=[-1]*n
        st=[]

        for i in range(n-1,-1,-1):
            while len(st) != 0 and st[-1]<=nums2[i]:
                st.pop()
        
            if len(st) != 0:
                nge[i] = st[-1]

            st.append(nums2[i])  

        # Get results for nums1
        res=[]
        for i in nums1:
            idx=nums2.index(i)
            res.append(nge[idx])
        return res          
                         