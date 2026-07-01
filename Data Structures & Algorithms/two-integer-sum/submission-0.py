class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = dict()
        for i, num in enumerate(nums):
            required = target - num
            if required in seen:
                return [seen[required], i]

            if num in seen: continue
            seen[num] = i

        return [-1, -1]
        