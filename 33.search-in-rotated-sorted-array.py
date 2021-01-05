#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (35.47%)
# Likes:    6599
# Dislikes: 579
# Total Accepted:    879.4K
# Total Submissions: 2.5M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# You are given an integer array nums sorted in ascending order, and an integer
# target.
# 
# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e.,
# [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# If target is found in the array return its index, otherwise, return -1.
# 
# 
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is guranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            
            mid = left + (right - left) // 2
            if nums[mid] == target: 
                return mid
                
            # case-1: un-rotated
            
            if nums[left] < nums[right]:
               
                if nums[mid] < target: left = mid + 1
                else: right = mid - 1
                    
            # case-2: rotated
            elif nums[mid] >= nums[left]:
                
                if nums[left] <=  target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:
                if  nums[mid] < target <= nums[right]:
                    left = mid + 1
                else: 
                    right = mid - 1
        
        return -1
       
# @lc code=end

