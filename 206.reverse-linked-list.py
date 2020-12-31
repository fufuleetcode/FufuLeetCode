#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (64.44%)
# Likes:    5870
# Dislikes: 113
# Total Accepted:    1.2M
# Total Submissions: 1.9M
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        # Solution-1: iteration
        # if not head:
        #     return head
        
        # new_head = head
        # while head.next:
        #     p = head.next
        #     head.next = p.next
        #     p.next = new_head
        #     new_head = p
        # return new_head


        # Solution-2: recursion

        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
        
# @lc code=end

