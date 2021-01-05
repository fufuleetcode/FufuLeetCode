#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (50.47%)
# Likes:    9396
# Dislikes: 142
# Total Accepted:    641K
# Total Submissions: 1.3M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
# 
# 
# Example 1:
# 
# 
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
# 
# 
# Example 2:
# 
# 
# Input: height = [4,2,0,3,2,5]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 0 <= n <= 3 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:

        # # Solution-1: DP with O(2n) = O(n)
        # # edge case handling
        # if not height: return 0
        
        # # DP to calculate leftMax and rightMax
        # leftMax = [0] * len(height)
        # leftMax[0] = height[0]
        # for i in range(1,len(height)):
        #     leftMax[i] = max(leftMax[i-1], height[i])
        
        # rightMax = [0] * len(height)
        # rightMax[-1] = height[-1]
        # for i in range(len(height)-2,-1,-1):
        #     rightMax[i] = max(rightMax[i+1], height[i])
        
        # # find the max
        # res = 0
        # for i in range(len(height)):
        #     res += min(rightMax[i], leftMax[i]) - height[i]
        # return res



        # Solution-2: two-pointer with O(n)

        if not height: return 0

        leftMax = 0
        rightMax = 0
        l = 0
        r = len(height) - 1
        res = 0
        while l <= r:


            if leftMax <= rightMax:

                res += max(0, leftMax - height[l])
                
                leftMax = max(leftMax, height[l])
                l += 1
            
            else:

                res += max(0, rightMax - height[r])
                
                rightMax = max(rightMax, height[r])
                r -= 1
        
        return res

    
# @lc code=end

