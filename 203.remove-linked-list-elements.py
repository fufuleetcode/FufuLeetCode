#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (38.98%)
# Likes:    2245
# Dislikes: 111
# Total Accepted:    413.1K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
# 
# Example:
# 
# 
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        # Solution 1
        # dummy_head = ListNode(0)
        # dummy_head.next = head
        # prev = dummy_head
        # curr = head

        # while curr:

        #     if curr.val != val:
        #         prev, curr = curr, curr.next
        #     else:
        #         prev.next = curr.next
        #         curr = curr.next
            
        # return dummy_head.next

        # Solution-2: recursion

        # if not head: return head

        # head.next = self.removeElements(head.next, val)
        # if head.val == val:
        #     return head.next
        # else:
        #     return head


        # Solution 2
        if not head: return head
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            return head.next
        else:
            return head
            
# @lc code=end

