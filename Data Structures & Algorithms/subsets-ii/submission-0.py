class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res= []
        def solve(index, subseq):
            if index >= len(nums):
                res.append(subseq.copy())
                return
            subseq.append(nums[index])
            solve(index + 1, subseq)
            subseq.pop()
            next_index = index + 1
            while next_index < len(nums) and nums[next_index] == nums[index]:
                next_index += 1
            solve(next_index, subseq)
        solve(0, [])
        return res


            
                        
        