class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_bucket: dic[tuple, List[str]] = {}
        frequency_arr = [0] * 26
        for s in strs:
            for char in s:
                frequency_arr[ord(char) - ord('a')] += 1

            frequency_tuple = tuple(frequency_arr)
            if frequency_tuple in anagram_bucket:
                anagram_bucket[frequency_tuple].append(s)
            else:
                anagram_bucket[frequency_tuple] = [s]

            frequency_arr = [0] * 26

        return list(anagram_bucket.values())
        