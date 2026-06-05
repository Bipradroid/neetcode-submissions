class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if target in triplets:
            return True

        valid = []

        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                valid.append(t)

        res = []

        for i in range(3):
            col = []
            for j in range(len(valid)):
                col.append(valid[j][i])

            if not col:
                return False

            res.append(max(col))

        return res == target

            

        