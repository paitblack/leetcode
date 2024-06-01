class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        x = str(x)
        reversed = str(x)[::-1]

        if x == reversed:
            return True
        else:
            return False
        