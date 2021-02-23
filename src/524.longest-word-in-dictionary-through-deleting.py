#
# @lc app=leetcode id=524 lang=python3
#
# [524] Longest Word in Dictionary through Deleting
#

# @lc code=start
# TAGS: Two Pointers, Sort
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def custom_sort(val):
            return -len(val), val
        d.sort(key=custom_sort)
        
        def compare(word):
            i = 0
            for c in s:
                if i < len(word) and c == word[i]:
                    i += 1
            return i == len(word)
        
        for word in d:
            if compare(word): return word
        return ''
                    
# @lc code=end

