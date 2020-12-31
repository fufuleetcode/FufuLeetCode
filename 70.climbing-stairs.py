#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (48.40%)
# Likes:    5563
# Dislikes: 177
# Total Accepted:    844.3K
# Total Submissions: 1.7M
# Testcase Example:  '2'
#
# You are climbing a staircase. It takes n steps to reach the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# 
# 
# Example 2:
# 
# 
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 45
# 
# 
#

# @lc code=start
class Solution:

    def __init__(self):
        # base case for cursion
        self.cache = {0:1, 1:1}

    def climbStairs(self, n: int) -> int:

        # use cache
        if n in self.cache:
            return self.cache[n]

        # recursion relation
        res = self.climbStairs(n-1) + self.climbStairs(n-2)

        # update cache
        self.cache[n] = res
        return res

        
        
# @lc code=end

