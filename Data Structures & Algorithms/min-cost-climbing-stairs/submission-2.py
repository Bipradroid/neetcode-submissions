class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[-1]*len(cost)
        def algo(index):
            dp[0]=cost[0]
            dp[1]=cost[1]
            for i in range(2,len(cost)):
                dp[i]=cost[i]+min(dp[i-1],dp[i-2])
            return dp[index]

        return min(algo(len(cost)-1),algo(len(cost)-2))
        