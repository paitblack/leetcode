class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            reversed_str = str(x)[::-1]
        else:
            reversed_str = "-" + str(x)[1:][::-1]

        reversed_num = int(reversed_str)
        
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0

        return reversed_num

        