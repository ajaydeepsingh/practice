class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        # brute force
        # generate all possible permutations O(2^n)
        
        
        # bottom-up dp O(n^2)
        
        # initialize dp array to 1
        # subarray 0 to index 
        
        
        if not nums:
            return 0
        
        n = len(nums)
        
        dp = [1] * n
        
        
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    
        
        return max(dp)
