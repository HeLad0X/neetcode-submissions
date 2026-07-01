from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        left_product = [1] * len(nums)
        right_product = [1] * len(nums)

        curr_product = 1
        i = 0
        while i < len(nums):
            left_product[i] = curr_product
            curr_product *= nums[i]
            i += 1

        i -= 1
        curr_product = 1
        while i >= 0:
            right_product[i] = curr_product
            curr_product *= nums[i]
            i -= 1

        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = left_product[i] * right_product[i]

        return res
