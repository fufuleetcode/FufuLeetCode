#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (56.90%)
# Likes:    1942
# Dislikes: 75
# Total Accepted:    572.8K
# Total Submissions: 1M
# Testcase Example:  '[1,null,2,3]'
#
# Given the root of a binary tree, return the preorder traversal of its nodes'
# values.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,null,2,3]
# Output: [1,2,3]
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: root = [1]
# Output: [1]
# 
# 
# Example 4:
# 
# 
# Input: root = [1,2]
# Output: [1,2]
# 
# 
# Example 5:
# 
# 
# Input: root = [1,null,2]
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# 
# 
# 
# 
# Follow up:
# 
# Recursive solution is trivial, could you do it iteratively?
# 
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
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        if not root: return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


        # Solution - 1: Iteration with Stack
        # 注意：一般recursion都可以使用stack来替换，因为recursion本身就是stack frame
        
        # edge case
        # if not root: return []

        # # initialize stack and result
        # stack = [root]
        # output = []

        # # iteration
        # while stack:
        #     root = stack.pop()
        #     output.append(root.val)
        #     if root.right:
        #         stack.append(root.right)
        #     if root.left:
        #         stack.append(root.left)
        # return output


        
# @lc code=end

