class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if j == len(p):
                return i == len(s)
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                result = dp(i, j + 2)
                if match:
                    result |= dp(i + 1, j)
            else:
                result = match and dp(i + 1, j + 1)
            memo[(i, j)] = result
            return result
        return dp(0, 0)