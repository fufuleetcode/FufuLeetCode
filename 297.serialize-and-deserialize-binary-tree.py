#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (49.10%)
# Likes:    3769
# Dislikes: 179
# Total Accepted:    393.6K
# Total Submissions: 800.5K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
# 
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
# 
# Clarification: The input/output format is the same as how LeetCode serializes
# a binary tree. You do not necessarily need to follow this format, so please
# be creative and come up with different approaches yourself.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
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
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Solution-1: BFS method, like the one in Leetcode example
# class Codec:

    # def serialize(self, root):
    #     """Encodes a tree to a single string.
        
    #     :type root: TreeNode
    #     :rtype: str
    #     """

    #     # edge case handling
    #     if not root: return ""


    #     res = []
    #     # queue for BFS
    #     from collections import deque
    #     Q = deque([root,])
        
    #     while Q:
    #         node = Q.popleft()

    #         # if the node is valid, then we use the standard BFS method,
    #         # note that the node.left and right are pushed to the queue even if they are None,
    #         # this is because we need None
    #         if node:
    #             res.append(str(node.val))
    #             Q.append(node.left)
    #             Q.append(node.right)
    #         else:
    #             res.append("")

    #     # furthr optimize the result by removing the None in the end
    #     while res and res[-1] == "":
    #         res.pop()

    #     res = ",".join(res)
    #     print(res)
    #     return res

    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.
        
    #     :type data: str
    #     :rtype: TreeNode
    #     """

    #     # edge case handling
    #     if data == "": return None

    #     # data is the wait-list
    #     # Q is the to-be-processed queue
    #     # let's repeast while the wait-list is not empty.
    #     # it's ok to quite if the Q is not empty, because we have trimmed the last Noen in the data in serializer

    #     from collections import deque
    #     data = deque([TreeNode(int(i)) if i != "" else None for i in data.split(",")])
    #     root = data.popleft()
    #     Q = deque([root])

    #     while data:
    #         node = Q.popleft()
    #         # the else case is to handle the trimmed None in data
    #         node.left = data.popleft() if data else None
    #         node.right = data.popleft() if data else None
    #         if node.left:
    #             Q.append(node.left)
    #         if node.right:
    #             Q.append(node.right)
    #     return root




# Solution-2: Preorder traversal
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        stack = [root]
        self.res = []

        def helper(node:"Treenode"):
            if node:
                self.res.append(str(node.val))
                helper(node.left)
                helper(node.right)
            else:
                self.res.append("")

        helper(root)
        self.res = ",".join(self.res)
        print(self.res)
        return self.res

                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "": return None
        from collections import deque
        data = deque([int(i) if i != "" else None for i in data.split(",")])
        def helper(data) -> TreeNode:
            node_val = data.popleft()
            if node_val is None:
                return None
            node = TreeNode(node_val)
            node.left = helper(data)
            node.right = helper(data)
            return node
        return helper(data)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

