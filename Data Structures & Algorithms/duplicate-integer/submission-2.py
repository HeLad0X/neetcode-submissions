class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2: return False
        num_set = set()
        for num in nums:
            if num in num_set: return True
            else:
                num_set.add(num)

        return False

        