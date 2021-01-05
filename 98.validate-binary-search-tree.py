#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (28.46%)
# Likes:    5176
# Dislikes: 617
# Total Accepted:    863.6K
# Total Submissions: 3M
# Testcase Example:  '[2,1,3]'
#
# Given the root of a binary tree, determine if it is a valid binary search
# tree (BST).
# 
# A valid BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [2,1,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        # Solution: divide and conquer with recursion
        # A tree if valid BST if the following three conditions are satisfied:
        # 1. left tree is valid BST
        # 2. right tree is valid BST
        # 3. left tree values all smaller than root.val
        # 4. right tree values all larger than root.val

        # Note that the defition by itself is recursive.
        def helper(root: TreeNode, lb:int, ub: int) -> bool:
            if not root: 
                return True
            
            if not lb < root.val < ub:
                return False
            
            return helper(root.left, lb, min(ub, root.val)) and helper(root.right, max(root.val, lb), ub)
        return helper(root, -float("inf"), float("inf"))

# @lc code=end

