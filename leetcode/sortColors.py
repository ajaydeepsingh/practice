class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
            
        counts = [0,0,0]
            
            
        for x in nums:
            if x == 0:
                counts[0] += 1
            elif x == 1:
                counts[1] += 1
            elif x == 2:
                counts[2] += 1
        
        
        index = 0
        while counts[0] > 0:
            nums[index] = 0
            index += 1
            counts[0] -= 1
        
        while counts[1] > 0:
            nums[index] = 1
            index += 1
            counts[1] -= 1
            
        while counts[2] > 0:
            nums[index] = 2
            index += 1
            counts[2] -= 1
            
            
            
        