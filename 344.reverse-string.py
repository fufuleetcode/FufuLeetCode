#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string/description/
#
# algorithms
# Easy (69.75%)
# Likes:    1895
# Dislikes: 740
# Total Accepted:    909K
# Total Submissions: 1.3M
# Testcase Example:  '["h","e","l","l","o"]'
#
# Write a function that reverses a string. The input string is given as an
# array of characters char[].
# 
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# You may assume all the characters consist of printable ascii characters.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# 
# 
# 
# Example 2:
# 
# 
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """


        def helper(s:List[str], i: int, j: int) -> None:

            if i >= j:
                return 
            
            s[i], s[j] = s[j], s[i]
            helper(s, i+1, j-1)
        
        helper(s, 0, len(s) - 1)
        return s
        
        
# @lc code=end

