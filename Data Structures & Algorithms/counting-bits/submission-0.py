class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        bit_list = list(range(0, n + 1))
        for m in bit_list:
            bit_m = list(map(int, bin(m)[2:]))
            res = 0
            for i in bit_m:
                res += i % 2
                i = i >> 1
            ans.append(res)
        return ans

            
        