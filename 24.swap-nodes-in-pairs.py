#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (51.86%)
# Likes:    3119
# Dislikes: 198
# Total Accepted:    552K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# You may not modify the values in the list's nodes. Only nodes itself may be
# changed.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# 
# 
# Example 2:
# 
# 
# Input: head = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: head = [1]
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        # Solution - 1: Recursion
        # terminal condition:
        #   None
        #   a --> None
        # if not head or not head.next:
        #     return head
        
        # # extract nodes
        # prev = head
        # curr = head.next
        # succ = head.next.next
        
        # # swap the prev and curr
        # prev.next = self.swapPairs(succ)
        # curr.next = prev
        # return curr



        # Solution - 2:  wihtout recursion, use iteration
        dummy_head = ListNode(0)
        dummy_head.next = head

        prev = dummy_head
        while head and head.next:

            first = head
            second = head.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            head = first.next


        return dummy_head.next
        
# @lc code=end

