#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (41.85%)
# Likes:    2710
# Dislikes: 194
# Total Accepted:    214.3K
# Total Submissions: 511.1K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1 ... n.
# 
# Example:
# 
# 
# Input: 3
# Output:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 8
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

    def helper(self, l: List[int]) -> List[TreeNode]:

        if not l:
            return [None]
        if len(l) == 1:
            return [TreeNode(l[0])]
        ll = len(l)
        res = []
        for rdx in range(ll):
            for left in self.helper(l[:rdx]):
                for right in self.helper(l[rdx+1:]):
                    root = TreeNode(l[rdx])
                    root.left = left
                    root.right = right
                    res.append(root)
        return res

    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return []
        return self.helper(range(1,n+1,1))

                


# @lc code=end

