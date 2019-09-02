def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        reference = set(nums)
        for x in range(0,len(nums)+1):
            if x not in reference:
                return x
            
        return True
        