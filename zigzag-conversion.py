class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows  
        direction = -1  
        row_index = 0  

        for char in s:
            rows[row_index] += char 
            if row_index == 0 or row_index == numRows - 1:
                direction *= -1  
            row_index += direction  

        return ''.join(rows) 
