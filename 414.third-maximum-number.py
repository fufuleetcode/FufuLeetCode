#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#
# https://leetcode.com/problems/third-maximum-number/description/
#
# algorithms
# Easy (30.57%)
# Likes:    828
# Dislikes: 1505
# Total Accepted:    189.3K
# Total Submissions: 619.2K
# Testcase Example:  '[3,2,1]'
#
# Given a non-empty array of integers, return the third maximum number in this
# array. If it does not exist, return the maximum number. The time complexity
# must be in O(n).
# 
# Example 1:
# 
# Input: [3, 2, 1]
# 
# Output: 1
# 
# Explanation: The third maximum is 1.
# 
# 
# 
# Example 2:
# 
# Input: [1, 2]
# 
# Output: 2
# 
# Explanation: The third maximum does not exist, so the maximum (2) is returned
# instead.
# 
# 
# 
# Example 3:
# 
# Input: [2, 2, 3, 1]
# 
# Output: 1
# 
# Explanation: Note that the third maximum here means the third maximum
# distinct number.
# Both numbers with value 2 are both considered as second maximum.
# 
# 
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        if not nums: 
            return None
        
        top_3_set = set()
        for num in nums:
            top_3_set.add(num)
            if len(top_3_set) > 3:
                top_3_set.remove(min(top_3_set))
        
        if len(top_3_set) == 3:
            return min(top_3_set)
        else:
            return max(top_3_set)

# @lc code=end

