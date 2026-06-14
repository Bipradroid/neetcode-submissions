class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for m in range(n + 1):
            bit_m = list(map(int, bin(m)[2:]))
            ans.append(sum(bit_m))

        return ans
        