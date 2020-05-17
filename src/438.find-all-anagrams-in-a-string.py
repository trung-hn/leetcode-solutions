#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# TAGS: Hash Table
# @lc code=start
class Solution:
    # 188 ms, 32%, Sliding window using Counter
    # Time: O(N_s + N_p), Space: O(N) but can be O(1) by using array
    def findAnagrams1(self, s: str, p: str) -> List[int]:
        size = len(p)
        base = collections.Counter(p)
        temp = collections.Counter(s[:size])
        ans = []
        s += "."
        for i in range(size, len(s)):
            if base == temp:
                ans.append(i-size)
            temp[s[i]] += 1 # Increase counter for new character
            temp[s[i - size]] -= 1 # Decrease counter for old character
            if temp[s[i - size]] == 0:
                del temp[s[i - size]]
        return ans
    
    # 108 ms, 84%, Sliding window using defaultdict
    # Time: O(N_s + N_p), Space: O(N) but can be O(1) by using array
    def findAnagrams(self, s: str, p: str) -> List[int]:
        base = collections.defaultdict(int)
        for c in p: base[c] += 1
        
        size = len(p) - 1
        temp = collections.defaultdict(int)
        for c in s[:size]: temp[c] += 1
        
        ans = []
        for i in range(size, len(s)):
            temp[s[i]] += 1 # Increase counter for new character
            if temp == base: ans.append(i-size)
            temp[s[i-size]] -= 1 # Decrease counter for old character
            if temp[s[i-size]] == 0: 
                del temp[s[i-size]] # remove key with Counter = 0 so we can compare dict
        return ans
# @lc code=end

