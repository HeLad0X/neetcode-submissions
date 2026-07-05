class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_num = sorted(nums)

        res = set()
        for i, num in enumerate(sorted_num):
            left = i + 1
            right = len(sorted_num) - 1
            while left < right:
                if sorted_num[left] + sorted_num[right] == -num:
                    triplet = tuple([num, sorted_num[left], sorted_num[right]])
                    res.add(triplet)
                    left += 1
                    right -= 1
                elif sorted_num[left] + sorted_num[right] > -num: right -= 1
                else: left += 1

        return list(res)
                