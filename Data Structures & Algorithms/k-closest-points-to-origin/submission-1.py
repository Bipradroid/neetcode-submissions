class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hashmap={}
        heap=[]
        for x,y in points:
            hashmap[(x,y)]=(x*x+y*y)**0.5
            heapq.heappush(heap,(hashmap[(x,y)], [x,y]))
        res=[]
        for _ in range(k):
            hashmap,point=heapq.heappop(heap)
            res.append(point)
        return res
        
        
        