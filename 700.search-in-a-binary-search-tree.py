#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/
#
# algorithms
# Easy (73.29%)
# Likes:    1186
# Dislikes: 124
# Total Accepted:    237.2K
# Total Submissions: 323.6K
# Testcase Example:  '[4,2,7,1,3]\n2'
#
# Given the root node of a binary search tree (BST) and a value. You need to
# find the node in the BST that the node's value equals the given value. Return
# the subtree rooted with that node. If such node doesn't exist, you should
# return NULL.
# 
# For example, 
# 
# 
# Given the tree:
# ⁠       4
# ⁠      / \
# ⁠     2   7
# ⁠    / \
# ⁠   1   3
# 
# And the value to search: 2
# 
# 
# You should return this subtree:
# 
# 
# ⁠     2     
# ⁠    / \   
# ⁠   1   3
# 
# 
# In the example above, if we want to search the value 5, since there is no
# node with value 5, we should return NULL.
# 
# Note that an empty tree is represented by NULL, therefore you would see the
# expected output (serialized tree format) as [], not null.
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
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if not root:
            return root
        
        if root.val == val:
            return root
        
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


        
# @lc code=end

