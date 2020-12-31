#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (47.77%)
# Likes:    4825
# Dislikes: 194
# Total Accepted:    566.5K
# Total Submissions: 1.2M
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of
# itself).”
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# 
# 
# Example 2:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
# of itself according to the LCA definition.
# 
# 
# Example 3:
# 
# 
# Input: root = [1,2], p = 1, q = 2
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q will exist in the tree.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        # Solution-1: Recursion
        # self.res = None
        
        # def helper( root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> bool:
            
        #     left_result = helper(root.left, p, q) if root.left else False
        #     right_result = helper(root.right, p, q) if root.right else False
        #     root_result = root == p or root == q

        #     if sum([int(left_result), int(right_result), int(root_result)]) == 2:
        #         self.res = root

        #     return left_result or right_result or root_result
        
        # helper(root, p, q)
        # return self.res



        # Solution-2: Iteration by firstly contructing a child --> parent dictionary, then create ancestor set for pointer p, then do similar for q and return the first common ancestor
        if not root: return root
        parents = {root:None}
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
                parents[node.right] = node
            if node.left:
                stack.append(node.left)
                parents[node.left] = node
        
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents[p]

        while q not in ancestors:
            q = parents[q]
        return q

            


# @lc code=end

