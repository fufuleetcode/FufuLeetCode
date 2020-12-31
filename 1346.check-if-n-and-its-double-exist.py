#
# @lc app=leetcode id=1346 lang=python3
#
# [1346] Check If N and Its Double Exist
#
# https://leetcode.com/problems/check-if-n-and-its-double-exist/description/
#
# algorithms
# Easy (36.57%)
# Likes:    262
# Dislikes: 43
# Total Accepted:    73.4K
# Total Submissions: 200.9K
# Testcase Example:  '[10,2,5,3]'
#
# Given an array arr of integers, check if there exists two integers N and M
# such that N is the double of M ( i.e. N = 2 * M).
# 
# More formally check if there exists two indices i and j such that :
# 
# 
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
# 
# 
# 
# Example 1:
# 
# 
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
# 
# 
# Example 2:
# 
# 
# Input: arr = [7,1,14,11]
# Output: true
# Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.
# 
# 
# Example 3:
# 
# 
# Input: arr = [3,1,7,11]
# Output: false
# Explanation: In this case does not exist N and M, such that N = 2 * M.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= arr.length <= 500
# -10^3 <= arr[i] <= 10^3
# 
# 
#

# @lc code=start
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        hash_table = set()

        for i in arr:

            if 2*i in hash_table or (i % 2 == 0 and i // 2 in hash_table):
                return True
            
            hash_table.add(i)
        
        return False
        
# @lc code=end

