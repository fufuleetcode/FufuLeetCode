#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (36.92%)
# Likes:    4683
# Dislikes: 183
# Total Accepted:    618K
# Total Submissions: 1.7M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
# 
# If target is not found in the array, return [-1, -1].
# 
# Follow up: Could you write an algorithm with O(log n) runtime complexity?
# 
# 
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # edge case handling
        if not nums: return [-1,-1]
        
        
        nums.append(nums[-1])
        # binary search for left boundary
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        # check if the boundary is correct, because it's possible that the target doesn't exist in the array.
        if nums[left] != target:
            return [-1,-1]
        
        # search for the right boundary (actually, it's searching for the starting point of first non-target element)
        right = len(nums)-1
        start = left
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            else:
                right = mid
        return [start, right - 1]

# @lc code=end

