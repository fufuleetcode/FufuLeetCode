#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
#
# algorithms
# Easy (46.14%)
# Likes:    3285
# Dislikes: 6152
# Total Accepted:    1.2M
# Total Submissions: 2.7M
# Testcase Example:  '[1,1,2]'
#
# Given a sorted array nums, remove the duplicates in-place such that each
# element appears only once and returns the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# Clarification:
# 
# Confused why the returned value is an integer but your answer is an array?
# 
# Note that the input array is passed in by reference, which means a
# modification to the input array will be known to the caller as well.
# 
# Internally you can think of this:
# 
# 
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
# 
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len
# elements.
# for (int i = 0; i < len; i++) {
# print(nums[i]);
# }
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2]
# Explanation: Your function should return length = 2, with the first two
# elements of nums being 1 and 2 respectively. It doesn't matter what you leave
# beyond the returned length.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4]
# Explanation: Your function should return length = 5, with the first five
# elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't
# matter what values are set beyond the returned length.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in ascending order.
# 
# 
#


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums: 
            return 0
        
        # left is the ptr to be the right boundary of non-dumplicated element.
        left = 0
        for right in range(len(nums)):
            if nums[right] == nums[left]:
                continue
            left += 1
            nums[left] = nums[right]
        return left + 1

        
# @lc code=end

