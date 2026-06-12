class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        space = [""] * 2 *n
        res = []
        def backtrack(space, total, index):
            if index >= 2*n:
                if total == 0:
                    res.append("".join(space))
                return
            if total > len(space)//2:
                return
            elif total < 0:
                return
            space[index] = "("
            sum = total + 1
            backtrack(space, sum , index + 1)
            space[index] = ")"
            sum = total - 1
            backtrack(space, sum, index + 1)
        backtrack(space, 0, 0)
        return res
             
            



        
        