class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
         s = {}

        for i, x in enumerate(nums):

        	complement = target - x

        	if complement in s:
        		return [s[complement], i]

        	s[x] = i

        return []