class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        for i in range(n):
            if count == 0:
                count +=1
                el= nums[i]
            elif nums[i] == el :
                count +=1

            else:
                count -=1
        count1 = 0
        for i in range(n):
            if nums[i] == el :
                count1 +=1 

        if count1 > n//2:
            return el               

        