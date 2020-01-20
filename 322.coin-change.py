#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (32.70%)
# Likes:    2823
# Dislikes: 96
# Total Accepted:    300.4K
# Total Submissions: 904.3K
# Testcase Example:  '[1,2,5]\n11'
#
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
# 
# Example 1:
# 
# 
# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# 
# Example 2:
# 
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# 
# Note:
# You may assume that you have an infinite number of each kind of coin.
# 
#

# @lc code=start
class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        """
        Solution-1: Recurtsion with memory
        """

        # mem = {}

        
        # def helper(coins, amount) -> int:
                
        #     if amount in mem: return mem[amount]
            
        #     if amount == 0: 
        #         mem[amount] = 0
        #         return 0
            
        #     res = sys.maxsize - 1
            
        #     for coin in coins:
        #         if amount >= coin: 
        #             this_res = helper(coins, amount - coin)
        #             if this_res == -1: 
        #                 continue
        #             else:
        #                 res = min(res, this_res + 1)
            
        #     if res == sys.maxsize-1:
        #         mem[amount] = -1
        #         return -1
            
        #     mem[amount] = res
        #     return res
        
        # return helper(coins, amount)   



        """
        Solution-2: Dynamic Programming.
        """

        dp = [sys.maxsize-1] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            if dp[i] == sys.maxsize-1:
                continue
            for coin in coins:
                if coin + i <= amount:
                    dp[coin + i] = min(dp[coin+i], dp[i] + 1)
        if dp[-1] == sys.maxsize-1: return -1
        return dp[-1]


# @lc code=end

