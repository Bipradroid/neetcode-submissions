class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product = float("-inf")
        for i in range(len(nums)):
            temp_prod = 1
            for j in range(i, len(nums)):
                temp_prod *= nums[j]
                product = max(product, temp_prod)
        return product
        