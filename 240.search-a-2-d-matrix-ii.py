#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (43.84%)
# Likes:    3982
# Dislikes: 86
# Total Accepted:    383.9K
# Total Submissions: 873.4K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n' +
  '5'
#
# Write an efficient algorithm that searches for a target value in an m x n
# integer matrix. The matrix has the following properties:
# 
# 
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# 
# 
# 
# Example 1:
# 
# 
# Input: matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 5
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 20
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -10^9 <= matix[i][j] <= 10^9
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      

      def helper(matrix:List[List[int]], row_low:int, row_high: int, col_low:int, col_high:int, target:int) -> bool:

        if row_low > row_high or col_low > col_high: return False

        row_mid = row_low + (row_high - row_low) // 2
        col_mid = col_low + (col_high - col_low) // 2

        if matrix[row_mid, col_mid] == target:
          return True
        elif matrix[row_mid, col_mid] < target:
          return helper(matrix, row_mid+1, row_high, col_low, col_mid, target) or 
                 helper(matrix, row_mid+1, row_high, col_mid+1, col_high, target) or 
                 helper(matrix, row_low, row_mid, col_mid+1, col_high, target)
        else:
          return helper(matrix, row_mid+1, row_high, col_low, col_mid, target) or 
                 helper(matrix, row_mid+1, row_high, col_mid+1, col_high, target) or 
                 helper(matrix, row_low, row_mid, col_mid+1, col_high, target)


        
# @lc code=end

