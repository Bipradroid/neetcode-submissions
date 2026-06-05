class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)% groupSize:
            return False
        
        hashmap={}
        for i in range(len(hand)):
            hashmap[hand[i]]=1+hashmap.get(hand[i],0)
        minheap=(list(hashmap.keys()))
        heapq.heapify(minheap)
        while minheap:
            first=minheap[0]
            for i in range(first,first+groupSize):
                if i not in hashmap:
                    return False
                hashmap[i]-=1
                if hashmap[i]==0:
                    if i!=minheap[0]:
                        return False
                    heapq.heappop(minheap)
        return True

            
        