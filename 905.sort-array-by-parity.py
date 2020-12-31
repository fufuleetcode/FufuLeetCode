#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#
# https://leetcode.com/problems/sort-array-by-parity/description/
#
# algorithms
# Easy (74.90%)
# Likes:    1430
# Dislikes: 80
# Total Accepted:    279.7K
# Total Submissions: 373.5K
# Testcase Example:  '[3,1,2,4]'
#
# Given an array A of non-negative integers, return an array consisting of all
# the even elements of A, followed by all the odd elements of A.
# 
# You may return any answer array that satisfies this condition.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
# 
# 
# 
#

# @lc code=start

# Two solutions, basically the same complexity, first is mine, second is LC

# Solution 1
# class Solution:
#     def sortArrayByParity(self, A: List[int]) -> List[int]:

#         if not A:
#             return []
        
#         left = 0
#         for right in range(len(A)):

#             if A[right] % 2 == 1:
#                 continue

#             A[left], A[right] = A[right], A[left]
#             left += 1
        
#         return A



# Solution 2
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        l, r = 0, len(A) - 1

        while l <= r:

            if A[l] % 2 > A[r] % 2:
                A[l], A[r] = A[r], A[l]
            

            if A[l] % 2 == 0:
                l += 1

            if A[r] % 2 == 1:
                r -= 1

        return A
        
# @lc code=end

