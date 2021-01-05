#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#
# https://leetcode.com/problems/clone-graph/description/
#
# algorithms
# Medium (38.04%)
# Likes:    2567
# Dislikes: 1586
# Total Accepted:    420.1K
# Total Submissions: 1.1M
# Testcase Example:  '[[2,4],[1,3],[2,4],[1,3]]'
#
# Given a reference of a node in a connected undirected graph.
# 
# Return a deep copy (clone) of the graph.
# 
# Each node in the graph contains a val (int) and a list (List[Node]) of its
# neighbors.
# 
# 
# class Node {
# ⁠   public int val;
# ⁠   public List<Node> neighbors;
# }
# 
# 
# 
# 
# Test case format:
# 
# For simplicity sake, each node's value is the same as the node's index
# (1-indexed). For example, the first node with val = 1, the second node with
# val = 2, and so on. The graph is represented in the test case using an
# adjacency list.
# 
# Adjacency list is a collection of unordered lists used to represent a finite
# graph. Each list describes the set of neighbors of a node in the graph.
# 
# The given node will always be the first node with val = 1. You must return
# the copy of the given node as a reference to the cloned graph.
# 
# 
# Example 1:
# 
# 
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val =
# 3).
# 
# 
# Example 2:
# 
# 
# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists
# of only one node with val = 1 and it does not have any neighbors.
# 
# 
# Example 3:
# 
# 
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.
# 
# 
# Example 4:
# 
# 
# Input: adjList = [[2],[1]]
# Output: [[2],[1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# Number of Nodes will not exceed 100.
# There is no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given
# node.
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    # Solution-1: DFS with recursion
    def cloneGraph_solution_1(self, node: 'Node') -> 'Node':
        # key is original node, value is new node
        # each time a node is visited, do the following thing:
        #   1. copy this node as node_cp, add node --> node_cp to self.visited
        #   2. build the pointer from node_cp to child_cp, where child_cp is the copy of neighbors of node.
        # 难点：edge是双向的，每次visit到的node，只需要构建这个node指向neighbors的指针即可，不然会重复。
    
        visited = dict()

        def dfs(node: 'Node', visited:dict):
            if not node: return None
            if node in visited:
                return visited[node]
            visited[node] = Node(node.val)
            for neighbor in node.neighbors:
                visited[node].neighbors.append(dfs(neighbor, visited))
            return visited[node]
        
        return dfs(node, visited)
    
    
    # Solution-2: DFS with iteration and stacks
    def cloneGraph_solution_2(self, node: 'Node') -> 'Node':

        if not node: return None

        node_cp = Node(node.val)
        visited = {node:node_cp}
        
        stack = [node]
        while stack:
            
            node = stack.pop()
            print(node.val)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                visited[node].neighbors.append(visited[neighbor])
        return node_cp

    # Solution-3: DFS with iteration and stacks
    def cloneGraph_solution_3(self, node: 'Node') -> 'Node':

        if not node: return None

        node_cp = Node(node.val)
        visited = {node:node_cp}
        
        from collections import deque
        Q = deque([node])
        while Q:
            print([i.val for i in Q])
            node = Q.popleft()
            print(node.val)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    Q.append(neighbor)
                visited[node].neighbors.append(visited[neighbor])
        return node_cp
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.cloneGraph_solution_1(node)
# @lc code=end

