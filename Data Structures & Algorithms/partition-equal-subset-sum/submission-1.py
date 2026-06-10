class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        dp = {}
        def find_sum(index, target):
            if target == 0:
                return True
            if index == 0:
                return nums[0] == target
            if target < 0:
                return False
            if (index , target) in dp:
                return dp[(index, target)]
            pick = find_sum(index - 1, target - nums[ index ])
            not_pick = find_sum(index - 1, target)

            dp[(index, target)] = pick or not_pick
            return dp[(index, target)]
        
        return find_sum(len(nums)-1,target)

        