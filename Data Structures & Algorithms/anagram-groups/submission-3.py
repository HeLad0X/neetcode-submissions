class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Note: Fixed typo 'dic' to 'dict' in type hinting
        anagram_bucket: dict[tuple, List[str]] = {}
        frequency_arr = [0] * 26
        
        for s in strs:
            for char in s:
                frequency_arr[ord(char) - ord('a')] += 1

            frequency_tuple = tuple(frequency_arr)
            anagram_bucket.setdefault(frequency_tuple, []).append(s)

            frequency_arr = [0] * 26

        return list(anagram_bucket.values())
