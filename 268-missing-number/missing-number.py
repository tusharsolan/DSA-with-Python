class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor1=0
        xor2=0
        n=len(nums)
        for i in range(n):
            xor2=xor2^nums[i]
            xor1=xor1^(i+1)
        #xor1=xor1^
        return xor1^xor2

        