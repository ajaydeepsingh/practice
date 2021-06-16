class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        i = 0
        j = len(height) - 1
        max_water = 0
        
        while i < j:
            
            width = j - i
            
            max_water = max(max_water, width * min(height[i], height[j]))
            
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        
        return max_water