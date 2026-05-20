class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Hashmap={}
        for i in range(len(nums)):
            Hashmap[nums[i]]=1+Hashmap.get(nums[i],0)
        sorted_hashmap=sorted(Hashmap.items(),key=lambda x: x[1],reverse=True)
        res=[]
        for i in range(k):
            res.append(sorted_hashmap[i][0])
        return res

