class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev0=cost[0]
        prev1=cost[1]
        for i in range(2,len(cost)):
            curr = cost[i] + min( prev0, prev1)
            prev0 = prev1
            prev1 = curr
        return min(prev0,prev1)
        
        