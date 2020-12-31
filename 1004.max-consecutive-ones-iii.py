#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#
# https://leetcode.com/problems/max-consecutive-ones-iii/description/
#
# algorithms
# Medium (60.32%)
# Likes:    1694
# Dislikes: 29
# Total Accepted:    79.8K
# Total Submissions: 132.2K
# Testcase Example:  '[1,1,1,0,0,0,1,1,1,1,0]\n2'
#
# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
# 
# Return the length of the longest (contiguous) subarray that contains only
# 1s. 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6
# Explanation: 
# [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is
# underlined.
# 
# 
# Example 2:
# 
# 
# Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# Output: 10
# Explanation: 
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is
# underlined.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 20000
# 0 <= K <= A.length
# A[i] is 0 or 1 
# 
# 
# 
#

# @lc code=start
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:

        l, r, zeros = 0, 0, 0

        res = 0
        while r < len(A):

            # print(l, r, zeros)

            res = max(res, r - l)

            if zeros < K:

                if A[r] == 0:
                    zeros += 1
                r += 1
                continue
            
            if A[r] == 1:
                r += 1
            else:

                if A[l] == 1:
                    l += 1
                else:
                    l += 1
                    zeros -= 1
        res = max(res, len(A) - l)
        return res
        
        
# @lc code=end

