#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#
# https://leetcode.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (72.35%)
# Likes:    1819
# Dislikes: 109
# Total Accepted:    377.1K
# Total Submissions: 521.2K
# Testcase Example:  '[-4,-1,0,3,10]'
#
# Given an integer array nums sorted in non-decreasing order, return an array
# of the squares of each number sorted in non-decreasing order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# 
# 
# Example 2:
# 
# 
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.
# 
# 
#

# @lc code=start



# Solution-1 (My First solution)
# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:

#         if not nums:
#             return []
        
#         # square for left and right array respectively.
#         left_array, right_array = [], []
#         for num in nums:
#             if num < 0:
#                 left_array.append(num**2)
#             else:
#                 right_array.append(num**2)
        
#         # reverse the order
#         left_array = left_array[::-1]

#         # merge sort.
#         res = []
#         left_ptr, right_ptr = 0, 0
#         while left_ptr < len(left_array) and right_ptr < len(right_array):
#             if left_array[left_ptr] < right_array[right_ptr]:
#                 res.append(left_array[left_ptr])
#                 left_ptr += 1
#             else:
#                 res.append(right_array[right_ptr])
#                 right_ptr += 1
        
#         if left_ptr < len(left_array):
#             res.extend(left_array[left_ptr:])
        
#         if right_ptr < len(right_array):
#             res.extend(right_array[right_ptr:])
        
#         return res
# The complexity of the solution is O(n), because merge sort's complexity is O(n1 + n2) = O(n)





# Solution-2 (Leetcode solution, same compelxity, but more short because it use two pointers and iterate for only one time)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        left_ptr = 0
        right_ptr = len(nums) - 1

        res = []
        while left_ptr <= right_ptr:
            if abs(nums[left_ptr]) <= abs(nums[right_ptr]):
                res.append(nums[right_ptr] ** 2)
                right_ptr -= 1
            else:
                res.append(nums[left_ptr] ** 2)
                left_ptr += 1
        return res[::-1]

# @lc code=end

