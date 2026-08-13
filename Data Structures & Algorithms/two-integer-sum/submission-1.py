class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = dict()

        for i, num in enumerate(nums):
            difference = target - num
            if difference in diff_dict: return [diff_dict[difference], i]
            else: diff_dict[num] = i

        return [-1, -1]
        