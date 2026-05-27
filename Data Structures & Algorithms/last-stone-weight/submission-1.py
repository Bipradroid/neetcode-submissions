class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]*=-1
        heapq.heapify(stones)
        while len(stones)>1:
            max_weight=heapq.heappop(stones)
            second_max_weight=heapq.heappop(stones)
            if max_weight==second_max_weight:
                continue
            else:
                heapq.heappush(stones,(max_weight-second_max_weight))
        if stones:
            return stones[0]*(-1)
        else:
            return 0
        