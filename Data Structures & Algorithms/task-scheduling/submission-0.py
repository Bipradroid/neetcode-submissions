class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        MaxHeap=[-cnt for cnt in count.values()]
        heapq.heapify(MaxHeap)
        q=collections.deque()
        time=0
        while MaxHeap or q:
            time+=1
            if MaxHeap:
                cnt=1+heapq.heappop(MaxHeap)
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                heapq.heappush(MaxHeap,q.popleft()[0])
        return time
        