def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        
        top = [0] * len(grid)
        leftRight = [0] * len(grid[0])
        
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                leftRight[i] = max(leftRight[i], grid[i][j])
                top[j] = max(top[j], grid[i][j])  
                
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += min(leftRight[i], top[j]) - grid[i][j]
                
        return res