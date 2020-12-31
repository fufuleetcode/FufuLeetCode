#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (47.71%)
# Likes:    5281
# Dislikes: 128
# Total Accepted:    784.9K
# Total Submissions: 1.6M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# 
# But the following [1,2,2,null,3,null,3] is not:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# Follow up: Solve it both recursively and iteratively.
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

    # Solution - 1: recursion (DFS)
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     if not root: return True
    #     return self.isMirror(root, root)
        
        
    # def isMirror(self, root1: TreeNode, root2: TreeNode) -> bool:
    #     if not root1 and not root2: return True        
    #     if not (root1 and root2): return False
    #     return  (root1.val == root2.val) and self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)


    # Solution - 2: queue (like BFS)
    # def isSymmetric(self, root: TreeNode) -> bool:

    #     from collections import deque
    #     queue = deque([root, root])

    #     while queue:

    #         t1 = queue.popleft()
    #         t2 = queue.popleft()

    #         if not t1 and not t2:
    #             continue

    #         if not (t1 and t2):
    #             return False
            
    #         if t1.val != t2.val:
    #             return False
            
    #         queue.append(t1.left)
    #         queue.append(t2.right)
    #         queue.append(t1.right)
    #         queue.append(t2.left)
        
    #     return True

    # Solution - 2:  DFS with stack
    def isSymmetric(self, root: TreeNode) -> bool:

        stack = [root, root]
        while stack:
            t1 = stack.pop()
            t2 = stack.pop()

            if not t1 and not t2:
                continue
            if not (t1 and t2):
                return False
            if t1.val != t2.val:
                return False
            stack.append(t1.left)
            stack.append(t2.right)
            stack.append(t1.right)
            stack.append(t2.left)
        return True

# @lc code=end

