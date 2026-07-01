from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        products = [1] * len(nums)

        curr_product = 1
        i = 0
        while i < len(nums):
            products[i] = curr_product
            curr_product *= nums[i]
            i += 1

        i -= 1
        curr_product = 1
        while i >= 0:
            products[i] *= curr_product
            curr_product *= nums[i]
            i -= 1

        return products
