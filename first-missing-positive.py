class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(num for num in nums if num > 0)
        
        smallest_positive = 1
        while smallest_positive in nums:
            smallest_positive += 1
        
        return smallest_positive
        


        