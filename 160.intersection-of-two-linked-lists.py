#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (42.33%)
# Likes:    4579
# Dislikes: 522
# Total Accepted:    558.5K
# Total Submissions: 1.3M
# Testcase Example:  '8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3'
#
# Write a program to find the node at which the intersection of two singly
# linked lists begins.
# 
# For example, the following two linked lists:
# 
# 
# begin to intersect at node c1.
# 
# 
# 
# Example 1:
# 
# 
# 
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA =
# 2, skipB = 3
# Output: Reference of the node with value = 8
# Input Explanation: The intersected node's value is 8 (note that this must not
# be 0 if the two lists intersect). From the head of A, it reads as
# [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes
# before the intersected node in A; There are 3 nodes before the intersected
# node in B.
# 
# 
# 
# Example 2:
# 
# 
# 
# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3,
# skipB = 1
# Output: Reference of the node with value = 2
# Input Explanation: The intersected node's value is 2 (note that this must not
# be 0 if the two lists intersect). From the head of A, it reads as
# [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes
# before the intersected node in A; There are 1 node before the intersected
# node in B.
# 
# 
# 
# 
# Example 3:
# 
# 
# 
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: null
# Input Explanation: From the head of A, it reads as [2,6,4]. From the head of
# B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must
# be 0, while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.
# 
# 
# 
# 
# Notes:
# 
# 
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function
# returns.
# You may assume there are no cycles anywhere in the entire linked
# structure.
# Each value on each linked list is in the range [1, 10^9].
# Your code should preferably run in O(n) time and use only O(1) memory.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        

        # nodeA = headA
        # nodeB = headB
        # nodeArestarted = False
        # nodeBrestarted = False
        
        # while nodeA and nodeB:

        #     if nodeA == nodeB:
        #         return nodeA
            
        #     if not nodeA.next and not nodeArestarted:
        #         nodeA = headB
        #         nodeArestarted = True
        #     else:
        #         nodeA = nodeA.next

        #     if not nodeB.next and not nodeBrestarted:
        #         nodeB = headA
        #         nodeBrestarted = True
        #     else:
        #         nodeB = nodeB.next
            
        # return None

        nodeA = headA
        nodeB = headB

        while nodeA != nodeB:

            if nodeA:
                nodeA = nodeA.next
            else:
                nodeA = headB
            
            if nodeB:
                nodeB = nodeB.next
            else:
                nodeB = headA

        return nodeA

# @lc code=end

