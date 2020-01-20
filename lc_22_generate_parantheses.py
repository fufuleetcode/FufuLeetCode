#LeetCode 22. Generate Parentheses

Solution-1: 
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        if n == 0: return [""]
        
        ans = []
        
        for c in range(n):
            
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - 1 - c):
                    ans.append("(" + left + ")" + right)
        
        return ans
    
                    
        
"""
Solution-2:Backtracking
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        
        def backtrack(S = "", left = 0, right = 0 ):
            
            
            if len(S) == 2 * n:
                
                ans.append(S)
            
            else:
                
                if left < n:
                    backtrack(S + "(", left+1,right)
                
                if left > right:
                    backtrack(S + ")", left, right + 1)
        
        backtrack("",0,0)
        return ans
                
                
