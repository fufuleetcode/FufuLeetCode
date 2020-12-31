#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#
# https://leetcode.com/problems/design-linked-list/description/
#
# algorithms
# Medium (25.48%)
# Likes:    708
# Dislikes: 798
# Total Accepted:    88.9K
# Total Submissions: 348.8K
# Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\n' + '[[],[1],[3],[1,2],[1],[1],[1]]'
#
# Design your implementation of the linked list. You can choose to use a singly
# or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val
# is the value of the current node, and next is a pointer/reference to the next
# node.
# If you want to use the doubly linked list, you will need one more attribute
# prev to indicate the previous node in the linked list. Assume all nodes in
# the linked list are 0-indexed.
# 
# Implement the MyLinkedList class:
# 
# 
# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the index^th node in the linked list. If
# the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of
# the linked list. After the insertion, the new node will be the first node of
# the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the
# linked list.
# void addAtIndex(int index, int val) Add a node of value val before the
# index^th node in the linked list. If index equals the length of the linked
# list, the node will be appended to the end of the linked list. If index is
# greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the index^th node in the linked list, if
# the index is valid.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get",
# "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]
# 
# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3
# 
# 
# 
# Constraints:
# 
# 
# 0 <= index, val <= 1000
# Please do not use the built-in LinkedList library.
# At most 2000 calls will be made to get, addAtHead, addAtTail,  addAtIndex and
# deleteAtIndex.
# 
# 
#

# @lc code=start
class ListNode:
    
    def __init__(self, x):
        
        self.val = x
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        # print(self)
        
    
    def __str__(self):
        node = self.head.next
        res = "(head)-->"
        while node != self.tail:
            res += str(node.val) + "-->"
            node = node.next
        res += "(tail)"
        return res
    

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # invalid case
        if index < 0 or index >= self.size:
            return -1
        
        node = None
        if index < self.size // 2:
            node = self.head
            for _ in range(index+1):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.size - index):
                node = node.prev
        # print(self)
        return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        prev, succ = self.head, self.head.next
        to_add = ListNode(val)
        to_add.next = succ
        to_add.prev = prev
        prev.next = to_add
        succ.prev = to_add
        self.size += 1
        # print(self)
        return
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        prev, succ = self.tail.prev, self.tail
        to_add = ListNode(val)
        to_add.next = succ
        to_add.prev = prev
        prev.next = to_add
        succ.prev = to_add
        self.size += 1
        # print(self)
        return 
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return
        
        node = None
        if index < self.size // 2:
            node = self.head
            for _ in range(index+1):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.size - index):
                node = node.prev
        
        prev = node.prev
        succ = node
        to_add = ListNode(val)
        to_add.next = succ
        to_add.prev = prev
        prev.next = to_add
        succ.prev = to_add
        self.size += 1
        # print(self)
        return
    
        
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        
        node = None
        if index < self.size // 2:
            node = self.head
            for _ in range(index+1):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.size - index):
                node = node.prev
        
        prev = node.prev
        succ = node.next
        prev.next = succ
        succ.prev = prev
        self.size -= 1
        # print(self)
        return 

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# @lc code=end

