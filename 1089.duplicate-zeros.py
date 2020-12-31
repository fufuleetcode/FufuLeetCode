#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
#
# https://leetcode.com/problems/duplicate-zeros/description/
#
# algorithms
# Easy (52.07%)
# Likes:    726
# Dislikes: 259
# Total Accepted:    110.4K
# Total Submissions: 212K
# Testcase Example:  '[1,0,2,3,0,4,5,0]'
#
# Given a fixed length array arr of integers, duplicate each occurrence of
# zero, shifting the remaining elements to the right.
# 
# Note that elements beyond the length of the original array are not written.
# 
# Do the above modifications to the input array in place, do not return
# anything from your function.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to:
# [1,0,0,2,3,0,0,4]
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3]
# Output: null
# Explanation: After calling your function, the input array is modified to:
# [1,2,3]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= arr.length <= 10000
# 0 <= arr[i] <= 9
# 
#

# @lc code=start
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        
        # Solution-1: My solution, not a good one as the complexity is O(n^2)
        # my idea is that, the index idx for loop through the entire array from left to right, if found zero value,
        # then will insert a zero to the right of it (which requires a shift of the rest of array)
        
        # if not arr:
        #     return 
        
        # idx = 0
        # while idx < len(arr):
            
        #     # if not 0, then skip,
        #     if arr[idx] != 0:
        #         idx += 1
        #         continue
            
        #     # if is 0, then shift the remaining elements.
        #     for jdx in range(len(arr)-2, idx, -1):
        #         arr[jdx+1] = arr[jdx]
                
        #     # insert to the right if there is still space.
        #     if idx+1 < len(arr):
        #         arr[idx+1] = 0
        #     idx += 2
        

        # Solution-2: better solution: Two pass, complexity O(n)

        possible_dup = 0
        length_ = len(arr) - 1

        # left is the left index pointer, last + possible_dup is the right index pointer that will try to locate the copied arr[left]
        # the idea is that, I will try to find the possible_dup (i.e. number of zeros to be copied in the copied version, note that it's not equal to the total number of zeros, because not all zeros will be kept in the result array)
        for left in range(len(arr)):

            # stop when the left item will be out of boundary in the duplicated version
            if left + possible_dup > length_:
                break
                
            if arr[left] == 0:
                
                # this is en edge case, this case is that, the 0 will be duplicated, but the first 0 is the last element (i.e. arr[length_], but the second will be trimmed, in this case, we will just copy here and ignore it, i.e. length -= 1)
                if left + possible_dup == length_:
                    arr[length_] = 0
                    length_ -= 1
                    break

                possible_dup += 1
        

        # last is the pointer of source
        # length is the pointer of destination.
        last = length_ - possible_dup
        for i in range(last, -1, -1):

            arr[length_] = arr[i]

            # shift the length_ by two if found zero.
            if arr[i] == 0:
                length_ -= 1
                arr[length_] = 0

            length_ -= 1

# @lc code=end

