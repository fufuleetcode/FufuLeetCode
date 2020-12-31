#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (38.98%)
# Likes:    4306
# Dislikes: 771
# Total Accepted:    489.3K
# Total Submissions: 1.3M
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]'
#
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
# 
# Return a deep copy of the list.
# 
# The Linked List is represented in the input/output as a list of n nodes. Each
# node is represented as a pair of [val, random_index] where:
# 
# 
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random
# pointer points to, or null if it does not point to any node.
# 
# 
# 
# Example 1:
# 
# 
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 
# 
# Example 2:
# 
# 
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
# 
# 
# Example 4:
# 
# 
# Input: head = []
# Output: []
# Explanation: Given linked list is empty (null pointer), so return null.
# 
# 
# 
# Constraints:
# 
# 
# -10000 <= Node.val <= 10000
# Node.random is null or pointing to a node in the linked list.
# The number of nodes will not exceed 1000.
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    # def __init__(self):
    #     self.visited_hash_map = dict()

    # def copyRandomList(self, head: 'Node') -> 'Node':

    #     if not head: return head

    #     if head in self.visited_hash_map:
    #         return self.visited_hash_map[head]

        
    #     head_cp = Node(head.val)
    #     self.visited_hash_map[head] = head_cp

    #     head_cp.next = self.copyRandomList(head.next)
    #     head_cp.random = self.copyRandomList(head.random)

    #     return head_cp


    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head: return head

        visited_hash_map = dict()

        node = head
        
        while node:

            # copy self
            if node not in visited_hash_map:
                visited_hash_map[node] = Node(node.val)
            
            # next
            if node.next not in visited_hash_map:
                visited_hash_map[node.next] = Node(node.next.val) if node.next else None
            visited_hash_map[node].next =  visited_hash_map[node.next]

            # random
            if node.random not in visited_hash_map:
                visited_hash_map[node.random] = Node(node.random.val) if node.random else None
            visited_hash_map[node].random = visited_hash_map[node.random] 

            node = node.next
        
        return visited_hash_map[head]





# @lc code=end

