#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
# TAGS: Hash Table, String, Pointers
# REVIEWME: Hash Table, String, Pointers
class Solution:
    # 9892 ms, 5.04%. Time: O(N^2)
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        freq = collections.Counter(words)
        total = len(words)
        W = len(words[0])
        ans = []
        def match(i, i0, cnt=0):
            if cnt == total:
                ans.append(i0)
                return
            if i >= len(s): return
            
            word = s[i : i + W]
            if freq[word] == 0: return
            freq[word] -= 1
            match(i + W, i0, cnt + 1)
            freq[word] += 1
            
        for i in range(len(s)):
            match(i, i)
        return ans
    
    # 100 ms, 81.05%. 2 pointers, 2 counters. Time: O(NK). Space: O(K)
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        freq = collections.Counter(words)
        word_len = len(words[0])
        total_len = word_len * len(words)
        ans = []
        for k in range(word_len):
            i = j = k
            curr = collections.Counter()
            while i + word_len <= len(s):
                word = s[i : i + word_len]
                i += word_len
                if word not in freq:
                    j = i
                    curr = collections.Counter()
                    continue
                    
                curr[word] += 1
                while curr[word] > freq[word]:
                    curr[s[j : j + word_len]] -= 1
                    j += word_len
                    
                if i - j == total_len:
                    ans.append(j)
        return ans
# @lc code=end

