#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#
# https://leetcode.com/problems/reconstruct-itinerary/description/
#
# algorithms
# Medium (33.27%)
# Likes:    1087
# Dislikes: 696
# Total Accepted:    107.3K
# Total Submissions: 321.6K
# Testcase Example:  '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# Given a list of airline tickets represented by pairs of departure and arrival
# airports [from, to], reconstruct the itinerary in order. All of the tickets
# belong to a man who departs from JFK. Thus, the itinerary must begin with
# JFK.
# 
# Note:
# 
# 
# If there are multiple valid itineraries, you should return the itinerary that
# has the smallest lexical order when read as a single string. For example, the
# itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# 
# 
# Example 1:
# 
# 
# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# 
# 
# Example 2:
# 
# 
# Input:
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is
# ["JFK","SFO","ATL","JFK","ATL","SFO"].
# But it is larger in lexical order.
# 
# 
#

# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = collections.defaultdict(dict)
        for u,v in tickets:
            if v not in g[u]:
                g[u][v] = 0
            g[u][v] += 1
        print(g)
        
        
        res = None
        def dfs(g, curr, path):
            
            nonlocal res
            
            if res :
                return
            
            if len(path) == len(tickets) + 1:
                res = path[:]
            
            for neighbor in sorted(g[curr].keys()):
                
                if g[curr][neighbor] == 0:
                    continue
                
                g[curr][neighbor]-=1
                path.append(neighbor)
                
                dfs(g, curr = neighbor, path = path)
                
                g[curr][neighbor] += 1
                path.pop()
            
        dfs(g, "JFK", ['JFK'])
        return res
# @lc code=end

