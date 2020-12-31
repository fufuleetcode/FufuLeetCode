#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (58.35%)
# Likes:    4722
# Dislikes: 147
# Total Accepted:    995.4K
# Total Submissions: 1.7M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Note:
# 
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        # .  .  .   .   . left.  .    .  . right 
        #   1  2  3   0   0  0  0  4    0  5
        #   1  2  3   4   5  0  0  0    0  0

        left = 0
        for right in range(len(nums)):

            if nums[right] == 0:
                continue

            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        
        return 

# @lc code=end

