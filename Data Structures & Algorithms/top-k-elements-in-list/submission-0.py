from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k >= len(set(nums)): return list(set(nums))

        counter = Counter(nums)
        return list([pair[0] for pair in counter.most_common(k)])