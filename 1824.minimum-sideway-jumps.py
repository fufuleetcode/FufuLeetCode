class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        
        
        dp = [1, 0, 1]
        
        for obstacle in obstacles:
            
            if obstacle:
                dp[obstacle-1] = float("inf")
            
            for y in range(3):
                
                if obstacle-1 != y:
                    dp[y] = min([dp[y], 1 + dp[(y+1)%3], 1 + dp[(y+2)%3]])
            
        return min(dp)
    
            
            