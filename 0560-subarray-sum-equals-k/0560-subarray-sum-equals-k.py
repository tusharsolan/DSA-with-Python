class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1  # for case when sum==k
        summ =0
        cnt =0
        for i in nums:
            summ+=i   #8
            if summ-k in d: #8-6 = 2
                cnt = cnt + d[summ-k]   #freq of 2 is 2 till now so cnt should be inc by 2

            d[summ]+=1 #inc the freq   # inc the d[8] by 1   , sum:freq


        return cnt
