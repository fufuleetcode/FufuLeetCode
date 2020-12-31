#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/
#
# algorithms
# Easy (74.27%)
# Likes:    571
# Dislikes: 136
# Total Accepted:    94.6K
# Total Submissions: 127.4K
# Testcase Example:  '[17,18,5,4,6,1]'
#
# Given an array arr, replace every element in that array with the greatest
# element among the elements to its right, and replace the last element with
# -1.
# 
# After doing so, return the array.
# 
# 
# Example 1:
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^4
# 1 <= arr[i] <= 10^5
# 
#

# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        max_element = -1
        for idx in range(len(arr)-1, -1, -1):
            curr = arr[idx]
            arr[idx] = max_element
            max_element = max(max_element, curr)
        return arr  
# @lc code=end

