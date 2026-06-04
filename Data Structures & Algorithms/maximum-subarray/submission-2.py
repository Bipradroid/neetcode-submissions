class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if all(x < 0 for x in nums):
            return max(nums)
        res=0
        for i in range(len(nums)):
            curr_res=0
            for j in range(i,len(nums)):
                curr_res+=nums[j]
                res=max(res,curr_res)
        return res

         
            



        