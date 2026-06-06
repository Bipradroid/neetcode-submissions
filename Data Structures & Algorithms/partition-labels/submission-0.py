class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap={}
        size=0
        end=0
        output=[]
        for i,c in enumerate(s):
            hashmap[c]=i
        for i,c in enumerate(s):
            size+=1
            end=max(end,hashmap[c])
            if i==end:
                output.append(size)
                size=0
        return output

        

        
        