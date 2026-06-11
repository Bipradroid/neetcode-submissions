class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def solve(index, subseq, total):
            if total == target:
                res.append(subseq.copy())
                return
            if total > target or index == len(nums):
                return
            subseq.append(nums[index])
            total = total + nums[index]
            solve(index, subseq, total)
            exit = subseq.pop()
            total = total - exit
            solve(index + 1, subseq, total)
        solve(0, [], 0)
        return res

            



        