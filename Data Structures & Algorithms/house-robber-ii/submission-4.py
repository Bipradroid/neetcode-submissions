class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums1=nums[:-1]
        nums2=nums[1:]
        dp1=[-1]*len(nums1)
        dp2=[-1]*len(nums2)
        def algo(nums,index,dp):
            dp[0]=nums[0]
            for i in range(1,len(nums)):
                if i>1:
                    pick=nums[i]+dp[i-2]
                else:
                    pick=nums[i]
                not_pick=dp[i-1]
                dp[i]=max(pick,not_pick)
            return dp[index]
        
        max1= algo(nums1,len(nums1)-1,dp1)
        max2=algo(nums2,len(nums2)-1,dp2)
        return max(max1,max2)