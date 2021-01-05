#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#
# https://leetcode.com/problems/sort-an-array/description/
#
# algorithms
# Medium (64.33%)
# Likes:    654
# Dislikes: 333
# Total Accepted:    117.7K
# Total Submissions: 182.7K
# Testcase Example:  '[5,2,3,1]'
#
# Given an array of integers nums, sort the array in ascending order.
# 
# 
# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000
# 
# 
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Solution-1: Merge Sort
        # merge sort terminal case
        # l = len(nums)
        # if l <= 1:
        #     return nums
        
        # left = nums[:(l // 2)][::]
        # right = nums[(l // 2):][::]

        # left = self.sortArray(left)
        # right = self.sortArray(right)

        # # merge two sorted list
        # res = []
        # i, j = 0, 0
        # while i < len(left) and j < len(right):
        #     if left[i] <= right[j]:
        #         res.append(left[i])
        #         i += 1
        #     else:
        #         res.append(right[j])
        #         j += 1
        # if i < len(left):
        #     res.extend(left[i:])
        # else:
        #     res.extend(right[j:])
        # return res

        # Solution-2: Quick sort
        def partition(nums:List[int], low_idx:int, high_idx:int) -> int:
            """
                partition nums[low_idx, high_idx+1], return the partition index location.
            """
            left = low_idx - 1
            pivot = high_idx 
            for right in range(low_idx, high_idx):
                if nums[pivot] <= nums[right]:
                    right += 1
                else:
                    left += 1
                    nums[right], nums[left] = nums[left], nums[right]
                    right += 1
            nums[left + 1], nums[pivot] = nums[pivot], nums[left+1]
            return left+1

        def quickSort(nums:List[int], low_idx:int, high_idx:int) -> None:
            if low_idx >= high_idx:
                return 
            pi = partition(nums, low_idx, high_idx)
            quickSort(nums, low_idx, pi-1)
            quickSort(nums, pi+1, high_idx)

        nums = nums[::]
        quickSort(nums, 0, len(nums) - 1)
        return nums

# @lc code=end

