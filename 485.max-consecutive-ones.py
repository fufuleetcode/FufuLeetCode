#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#
# https://leetcode.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (53.36%)
# Likes:    981
# Dislikes: 376
# Total Accepted:    320.5K
# Total Submissions: 600.7K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# Given a binary array, find the maximum number of consecutive 1s in this
# array.
# 
# Example 1:
# 
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive
# 1s.
# ⁠   The maximum number of consecutive 1s is 3.
# 
# 
# 
# Note:
# 
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
# 
# 
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        if not nums:
            return 0
            
        res = 0
        count = 0
        for idx in range(len(nums)):
            if nums[idx] == 0:
                res = max(res, count)
                count = 0
            else:
                count += 1
        res = max(res, count)
        return res
  
# @lc code=end

