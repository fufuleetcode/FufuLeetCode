#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (30.73%)
# Likes:    1984
# Dislikes: 3499
# Total Accepted:    571.4K
# Total Submissions: 1.9M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (i.e. x^n).
# 
# 
# Example 1:
# 
# 
# Input: x = 2.00000, n = 10
# Output: 1024.00000
# 
# 
# Example 2:
# 
# 
# Input: x = 2.10000, n = 3
# Output: 9.26100
# 
# 
# Example 3:
# 
# 
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 
# 
# Constraints:
# 
# 
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# -10^4 <= x^n <= 10^4
# 
# 
#

# @lc code=start
class Solution:

    def fastPow(self, x: float, n:int) -> float:

        # terminal case handling
        if n == 1:
            return x

        # recursive relation
        res = self.fastPow(x , n // 2)
        res = res * res
        if n % 2 == 1:
            res *= x

        return res

    def myPow(self, x: float, n: int) -> float:
        # edge case
        if n == 0: return 1.0

        # neg n handling
        is_neg_power = n < 0
        n = abs(n)

        # call helper
        res = self.fastPow(x, n)

        # handling neg n
        if is_neg_power:
            res = 1.0 / res
        return res
   
# @lc code=end

