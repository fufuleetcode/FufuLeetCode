#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (55.07%)
# Likes:    5588
# Dislikes: 687
# Total Accepted:    1.2M
# Total Submissions: 2.2M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new sorted list. The new
# list should be made by splicing together the nodes of the first two lists.
# 
# 
# Example 1:
# 
# 
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# 
# 
# Example 2:
# 
# 
# Input: l1 = [], l2 = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: l1 = [], l2 = [0]
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both l1 and l2 are sorted in non-decreasing order.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # Solution -1 Iteration
        # # create dummy head
        # dummy_head = ListNode(0)
        # new_tail = dummy_head

        # # keep appending the lowest node to the tail
        # while l1 and l2:
        #     if l1.val > l2.val:

        #         new_tail.next = l2
        #         l2 = l2.next
                
        #     else:

        #         new_tail.next = l1
        #         l1 = l1.next
            
        #     new_tail = new_tail.next
        
        # # append unfinished list to the tail
        # new_tail.next = l1 if l1 else l2
        # return dummy_head.next


        # Solution-2: recursion

        # edge case
        if not l1:
            return l2
        if not l2:
            return l1
        
        # recursion relation.
        if l2.val <= l1.val:
            l1, l2 = l2, l1
            
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

# @lc code=end

