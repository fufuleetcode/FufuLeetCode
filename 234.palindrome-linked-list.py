#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (40.04%)
# Likes:    4264
# Dislikes: 404
# Total Accepted:    522.7K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# 
# Input: 1->2
# Output: false
# 
# Example 2:
# 
# 
# Input: 1->2->2->1
# Output: true
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        # Solution - 1
        # node = head
        # l = []
        # while node:
        #     l.append(node.val)
        #     node = node.next
        # return l == l[::-1]
        
        
        
        
        # Solution - 2
        #         self.left_ptr = head
                
        #         def helper_is_parlindrome(node:ListNode) -> bool:
                    
        #             if not node:
        #                 return True
        #             if not helper_is_parlindrome(node.next):
        #                 return False
        #             if node.val != self.left_ptr.val:
        #                 return False
                    
        #             self.left_ptr = self.left_ptr.next
        #             return True
                
        #         return helper_is_parlindrome(head)


        # Solution - 3:
    
        # big picture is to reverse the second half of the linked list, then use two pointer (left and right) to compare starting from two end and move toward center.
        
        if not head or not head.next: return True
        
        
        # find the mid point "slow"
        slow, fast = head, head
        while  fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # print(slow.val, fast.val)
        
        # reverse the second half
        def reverse_ll(head:ListNode) -> ListNode:
            
            dummy_head = ListNode(0)
            dummy_head.next = head
            
            new_head = None
            while dummy_head.next:
                p = dummy_head.next
                dummy_head.next = p.next
                p.next = new_head
                new_head = p
            return new_head
        
        # reverse the right linked list
        right_rev = reverse_ll(slow.next)
        slow.next = None
        
        # compare and see if is palindrome
        l = head
        r = right_rev
        is_palindrome = True
        while l and r:
            if l.val != r.val:
                is_palindrome = False
                break
            l = l.next
            r = r.next
        
        # reverse back.
        right_orig = reverse_ll(right_rev)
        slow.next = right_orig
        return is_palindrome
            
# @lc code=end

