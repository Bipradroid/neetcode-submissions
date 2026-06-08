class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        nums1=nums[:-1]
        nums2=nums[1:]
        prev1_1=nums1[0]
        prev1_2=nums2[0]
        prev2_1, prev2_2=0,0
        def algo(nums,prev1,prev2):
            if not nums:
                return 0
            prev1=nums[0]
            prev2=0
            for i in range(1,len(nums)):
                if i>1:
                    pick=nums[i]+prev2
                else:
                    pick=nums[i]
                not_pick=prev1
                curr=max(pick,not_pick)
                prev2=prev1
                prev1=curr
            return prev1
        ans1=algo(nums1,prev1_1,prev2_1)
        ans2=algo(nums2,prev1_2,prev2_2)
        return max(ans1,ans2)

        