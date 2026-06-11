class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def solve(index, subarray):
            if index >= len(nums):
                res.append(subarray.copy())
                return
            subarray.append(nums[index])
            solve(index+1, subarray)
            subarray.pop()
            solve(index+1, subarray)
        solve(0, [])
        return res

        