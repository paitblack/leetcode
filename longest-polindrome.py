s = "aaaaaxbabxad"


def palindrome(s):
    last = ""

    for i in range(len(s)):
        # Check for odd length palindromes
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if len(s[left+1:right]) > len(last):
            last = s[left+1:right]
        
        # Check for even length palindromes
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if len(s[left+1:right]) > len(last):
            last = s[left+1:right]
    
    return last


print(palindrome(s))

