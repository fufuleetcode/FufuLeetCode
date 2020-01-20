class Solution:
    """
    Solution-1: O(nlog(n))
    """

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        def dist(x):
            return x[0]**2 + x[1]**2
        
        return heapq.nsmallest(K, points, key = dist)

    """
    Solution-2: O(nlog(k))
    """
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        points.sort(key = lambda x: x[0]**2 + x[1]**2)
        return points[:K]


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