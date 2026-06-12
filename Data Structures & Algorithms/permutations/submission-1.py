class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def solve(subseq):
            if len(subseq) == len(nums):
                res.append(subseq.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                subseq.append(nums[i])
                used[i] = True

                solve(subseq)

                subseq.pop()
                used[i] = False

        solve([])
        return res



        