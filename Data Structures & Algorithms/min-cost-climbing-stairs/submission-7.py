class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[-1]*len(cost)
        def algo(index):
            if index<2 and index>=0:
                return cost[index]
            if dp[index]!=-1:
                return dp[index]
            dp[index]= cost[index]+ min(algo(index-1),algo(index-2))
            return dp[index]

        return min(algo(len(cost)-1),algo(len(cost)-2))
        