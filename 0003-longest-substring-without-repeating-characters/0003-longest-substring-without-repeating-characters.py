class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        contains = {}
        start = 0

        for end, char in enumerate(s):
            if char in contains and contains[char] >= start:
                start = contains[char] + 1

            contains[char] = end
            current_length = end - start + 1
            longest = max(longest, current_length)

        return longest
