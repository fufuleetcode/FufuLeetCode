#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#
# https://leetcode.com/problems/fibonacci-number/description/
#
# algorithms
# Easy (67.16%)
# Likes:    942
# Dislikes: 211
# Total Accepted:    285.8K
# Total Submissions: 425.3K
# Testcase Example:  '2'
#
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
# Fibonacci sequence, such that each number is the sum of the two preceding
# ones, starting from 0 and 1. That is,
# 
# 
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# 
# 
# Given n, calculate F(n).
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# 
# 
# Example 2:
# 
# 
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# 
# 
# Example 3:
# 
# 
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 30
# 
# 
#

# @lc code=start
class Solution:

    def __init__(self):
        self.cache:Dict[int, int] = dict()

    def fib(self, n: int) -> int:

        #get cache result
        if n in self.cache:
            return self.cache[n]
        
        # compute F(n) = F(n-1) + F(n-2)
        res = None
        if n == 0:
            res = 0
        elif n == 1:
            res = 1
        else:
            res = self.fib(n-1) + self.fib(n-2)
        self.cache[n] = res
        return res
        
# @lc code=end

