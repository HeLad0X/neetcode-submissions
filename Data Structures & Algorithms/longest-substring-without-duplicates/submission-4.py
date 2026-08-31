class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        seen_char = dict()
        max_length = -1
        left = 0

        for right, ch in enumerate(s):
            if ch in seen_char and seen_char[ch] >= left:
                left = seen_char[ch] + 1

            seen_char[ch] = right
            max_length = max((right - left + 1), max_length)

        return max_length