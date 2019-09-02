def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        check = set()
        for x in nums:
            if x not in check:
                check.add(x)
            else:
                return True
        
        
        return False