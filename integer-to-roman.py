class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    
        roman_numeral = ""

        for i in range(len(roman_values)):

            while num >= roman_values[i]:
                roman_numeral += roman_symbols[i]
                num -= roman_values[i]

        return roman_numeral
            
