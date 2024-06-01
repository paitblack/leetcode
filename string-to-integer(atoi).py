class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.strip()  

        if not s:
            return 0

        numbers = "0123456789"
        sign = 1
        result = 0
        i = 0

        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        while i < len(s) and s[i] in numbers:
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1
        else:
            return result
        
        