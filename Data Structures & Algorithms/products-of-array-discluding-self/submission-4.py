class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0
        zero_index = -1
        for i, num in enumerate(nums):
            if num == 0 and zero_count == 0:
                zero_index = i
                zero_count = 1
                continue
            elif num == 0:
                return [0] * len(nums)

            total_product *= num

        if zero_index != -1:
            res = [0] * len(nums)
            res[zero_index] = total_product
            return res

        for i in range(len(nums)):
            nums[i] = total_product // nums[i]

        return nums


        