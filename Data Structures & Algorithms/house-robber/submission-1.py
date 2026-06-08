class Solution:
    def rob(self, nums: List[int]) -> int:
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

        