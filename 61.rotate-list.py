#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (31.42%)
# Likes:    1921
# Dislikes: 1101
# Total Accepted:    339.3K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, rotate the list to the right by k places.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# 
# 
# Example 2:
# 
# 
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 10^9
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
    def rotateRight(self, head: ListNode, k: int) -> ListNode:


        # Solution - 1: My solution, it's a little bit messy compared with the provided solution that use a ring to solve the problem.
        # if not head: return head

        # # simplify k to be in range [0, l)
        # l = 0
        # node = head
        # while node:
        #     node = node.next
        #     l += 1
        # k = k % l

        # if k == 0:
        #     return head
        
        # left = head
        # right = head
        # for _ in range(k):
        #     right = right.next
        # while right.next:
        #     left, right = left.next, right.next
        # pivot = left
        # new_head = pivot.next
        # left.next = None
        # right_tail = new_head
        # while right_tail.next:
        #     right_tail = right_tail.next
        # right_tail.next = head
        # return new_head

        # Solution - 2: Provided solution
        if not head: return head
        if not head.next: return head
        
        tail = head
        l = 1
        while tail.next:
            tail = tail.next
            l += 1
        
        tail.next = head

        k = k % l

        prev = tail
        curr = head
        for _ in range(l - k):
            prev, curr = curr, curr.next
        prev.next = None
        return curr
        
# @lc code=end

