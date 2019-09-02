# Given a non-empty array of integers, every element appears twice except for one.
# Find that single one.


    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = {}
        
        for x in nums:
            if x not in count:
                count[x] = 1
            elif x in count:
                count[x] += 1
          
        for k,v in count.items():
            if v == 1:
                return k
                
        ### More Clever
        # hash_table = {}
        # for i in nums:
        #     try:
        #         hash_table.pop(i)
        #     except:
        #         hash_table[i] = 1
        # return hash_table.popitem()[0]