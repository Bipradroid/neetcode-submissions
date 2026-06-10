class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product = []
        for i in range(len(nums)):
            temp_prod = 1
            for j in range(i, len(nums)):
                temp_prod *= nums[j]
                product.append(temp_prod)
        return max(product)
                
        