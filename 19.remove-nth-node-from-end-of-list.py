#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (35.52%)
# Likes:    4383
# Dislikes: 269
# Total Accepted:    750.6K
# Total Submissions: 2.1M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, remove the n^th node from the end of the
# list and return its head.
# 
# Follow up: Could you do this in one pass?
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [1], n = 1
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: head = [1,2], n = 1
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        

        # create dummy head
        dummy_head = ListNode(0)
        dummy_head.next = head
        
        # create two pointers left and right
        
        left = dummy_head
        right = dummy_head
        for _ in range(n):
            right = right.next
        
        # shift left and right
        while right.next:
            left = left.next
            right = right.next
        
        # delete prev.next
        prev = left
        succ = left.next.next
        prev.next = succ
        
        # return
        return dummy_head.next


# @lc code=end

