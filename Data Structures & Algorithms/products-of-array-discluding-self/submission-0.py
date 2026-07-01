from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        total_product = 1
        zero_count = 0
        zero_index = -1
        for i, num in enumerate(nums):
            if num == 0:
                if zero_count > 0:
                    return [0] * len(nums)

                zero_count = 1
                zero_index = i
                continue

            total_product *= num

        if zero_index > -1:
            res = [0] * len(nums)
            res[zero_index] = total_product
            return res

        for i, num in enumerate(nums):
            nums[i] = int(total_product / num)

        return nums

