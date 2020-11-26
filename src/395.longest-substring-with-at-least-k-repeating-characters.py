#
# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#

# @lc code=start
# TAGS: Divide and Conquer, Recursion, Sliding Window
class Solution:
    # LTE. Time: O(N^2)
    def longestSubstring(self, s: str, k: int) -> int:
        def valid(counter, k):
            return all(c >= k for c in counter.values())
        
        ans = 0
        for i in range(len(s)):
            counter = collections.Counter()
            for j in range(i, len(s)):
                counter[s[j]] += 1
                if valid(counter, k):
                    ans = max(ans, j - i + 1)
        return ans
                    
    # Divide and conquer. 32 ms, 83.66%. 
    # Worst case is still O(N^2) but O(NlogN) on average
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k: # split here
                return max(self.longestSubstring(sub, k) for sub in s.split(c))
        return len(s)
# @lc code=end

