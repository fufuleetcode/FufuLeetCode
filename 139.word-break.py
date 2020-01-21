#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (37.48%)
# Likes:    3258
# Dislikes: 173
# Total Accepted:    445.3K
# Total Submissions: 1.2M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
# 
# Note:
# 
# 
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
# 
# 
# Example 2:
# 
# 
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
# 
# 
#

# @lc code=start
class Solution:


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        """
        Solution-0: BF Recursion
        """
        # def helper(s, curr_idx) -> bool:
                        
        #     if curr_idx == len(s) :
        #         return True
            
        #     N = len(s)
            
        #     for word in wordDict:
                                
        #         if len(word) <= N - curr_idx  and s[curr_idx:curr_idx+len(word)] in wordDict and helper(s,curr_idx+len(word)):
        #             return True
            
        #     return False
        
        # return helper(s, 0)
        

        """
        Solution-1: Recursion with memory
        """

        # mem  = {}
        # def helper(s, curr_idx) -> bool:
                        
        #     if curr_idx in mem:
        #         return mem[curr_idx]
            
        #     if curr_idx == len(s) :
        #         mem[curr_idx] = True
        #         return True
            
        #     N = len(s)
            
        #     for word in wordDict:
                                
        #         if len(word) <= N - curr_idx  and s[curr_idx:curr_idx+len(word)] in wordDict and helper(s,curr_idx+len(word)):
        #             mem[curr_idx] = True
        #             return True
            
        #     mem[curr_idx] = False
        #     return False
        
            
        # return helper(s, 0)    


        """
        Solution-2: BFS( time out limit error)
        """
        
        # queue = collections.deque([0])
        
        # while queue:
            
        #     idx = queue.popleft()
            
        #     # print(idx)
            
        #     if idx == len(s):
        #         return True
            
        #     for end in range(idx, len(s) ):
                
        #         if s[idx:end+1] in wordDict:
                    
        #             queue.append(end+1)
                
        # return False



        """
        Solution-3: Dynamic Programming
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            if dp[i]:
                for word in wordDict:
                    if s[i:i+len(word)] == word:
                        dp[i+len(word)] = True
        return dp[-1]


# @lc code=end

