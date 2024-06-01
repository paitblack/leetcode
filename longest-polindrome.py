class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def center(left,right):
            while (left >= 0 and right < (len(s))) and s[left]==s[right]:
                left = left-1
                right = right+1

            return s[left+1:right]

        last = ""

        for i in range(len(s)):
            for_odd = center(i,i)
            for_even = center(i,i+1)

            if len(for_odd) > len(last):
                last = for_odd
            if len(for_even) > len(last):
                last = for_even
    
        return last
