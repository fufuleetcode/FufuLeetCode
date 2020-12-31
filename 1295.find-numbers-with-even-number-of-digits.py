#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
#
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/
#
# algorithms
# Easy (79.58%)
# Likes:    512
# Dislikes: 66
# Total Accepted:    203.4K
# Total Submissions: 255.6K
# Testcase Example:  '[12,345,2,6,7896]'
#
# Given an array nums of integers, return how many of them contain an even
# number of digits.
# 
# Example 1:
# 
# 
# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.
# 
# 
# Example 2:
# 
# 
# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 1771 contains an even number of digits.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 500
# 1 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:

    def n_digits(self, num:int) -> int:
        res = 0
        while num > 0:
            num //= 10
            res += 1
        return res
    
    
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if self.n_digits(num) % 2 == 0:
                res += 1
        return res


        
# @lc code=end

