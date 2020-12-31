#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
# https://leetcode.com/problems/k-closest-points-to-origin/description/
#
# algorithms
# Medium (64.40%)
# Likes:    2504
# Dislikes: 132
# Total Accepted:    389.3K
# Total Submissions: 604.4K
# Testcase Example:  '[[1,3],[-2,2]]\n1'
#
# We have a list of points on the plane.  Find the K closest points to the
# origin (0, 0).
# 
# (Here, the distance between two points on a plane is the Euclidean
# distance.)
# 
# You may return the answer in any order.  The answer is guaranteed to be
# unique (except for the order that it is in.)
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation: 
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just
# [[-2,2]].
# 
# 
# 
# Example 2:
# 
# 
# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000
# 
# 
# 
#

# @lc code=start
class Solution:
    """
    Solution-1: O(nlog(n))
    """

    # def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
    #     def dist(x):
    #         return x[0]**2 + x[1]**2
        
    #     return heapq.nsmallest(K, points, key = dist)

    """
    Solution-2: O(nlog(k))
    """
    # def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
    #     points.sort(key = lambda x: x[0]**2 + x[1]**2)
    #     return points[:K]


    """
    Solution-3: O(n)
    """

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        def dist(x) -> int:
            return x[0]**2 + x[1] ** 2
        
        def partition(i,j)->int:
            pivot = points[j]
            l = i - 1
            for r in range(i,j):
                rv = points[r]
                # print(r, points)
                if dist(rv) < dist(pivot):
                    l += 1
                    points[l], points[r] = points[r], points[l]
            points[j], points[l+1] = points[l+1], points[j]
            return l+1
        
        
        def sort(i,j,K):
            if i >= j: return 
            
            mid = partition(i,j)
            if (mid - i + 1) == K:
                return
            elif (mid - i + 1) < K:
                sort(mid + 1, j, K - (mid - i + 1))
            else:
                sort(i, mid - 1, K)
        
        sort(0, len(points)-1, K)
        return points[:K]

# @lc code=end

