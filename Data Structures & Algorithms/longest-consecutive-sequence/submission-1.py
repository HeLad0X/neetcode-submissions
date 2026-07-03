from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        counter = Counter(nums)
        start_set = set()

        for num in counter:
            if num - 1 not in counter: start_set.add(num)

        curr_length = 1
        max_length = -1
        for num in start_set:
            next_val = num + 1
            while next_val in counter: 
                curr_length += 1
                next_val += 1

            max_length = max(curr_length, max_length)
            curr_length = 1

        return max_length
