class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums1=nums[:-1]
        nums2=nums[1:]
        dp1=[-1]*len(nums1)
        dp2=[-1]*len(nums2)
        def algo(nums,index,dp):
            if index==0:
                return nums[0]
            if index<0:
                return 0
            if dp[index]!=-1:
                return dp[index]
            pick=nums[index]+algo(nums,index-2,dp)
            not_pick= algo(nums,index-1,dp)
            dp[index]= max(pick,not_pick)
            return dp[index]
        
        max1= algo(nums1,len(nums1)-1,dp1)
        max2=algo(nums2,len(nums2)-1,dp2)
        return max(max1,max2)
        