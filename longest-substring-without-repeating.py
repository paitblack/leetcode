class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0

        longest_len = 0
        start = 0
        char_index_map = {}

        for i in range(len(s)):
            if s[i] in char_index_map and char_index_map[s[i]] >= start:
                start = char_index_map[s[i]] + 1
            else:
                longest_len = max(longest_len, i - start + 1)

            char_index_map[s[i]] = i

        return longest_len
        