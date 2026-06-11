class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res= []
        def solve(index, total , subseq):
            if total == target:
                res.append(subseq.copy())
                return
            if total > target or index >= len(candidates):
                return
            subseq.append(candidates[index])
            total = total + candidates[index]
            solve(index + 1, total, subseq)
            exit = subseq.pop()
            total = total - exit
            next_index = index + 1
            while next_index < len(candidates) and candidates[index] == candidates[next_index]:
                next_index = next_index + 1            
            solve(next_index, total, subseq)
        solve(0, 0, [])
        return res

        