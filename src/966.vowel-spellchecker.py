#
# @lc app=leetcode id=966 lang=python3
#
# [966] Vowel Spellchecker
#

# @lc code=start
# TAGS: Hash Table, String
class Solution:
    # 192 ms, 42.86%. Time: O(N). Space: O(N)
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        word_dict = collections.defaultdict(str)
        for w in wordlist:
            word_dict[(0, w)] = w
            lower = w.lower() 
            if (1, lower) not in word_dict:
                word_dict[(1, lower)] = w
            no_vowels = "".join('.' if c in 'aeoiu' else c for c in w.lower())
            if (2, no_vowels) not in word_dict:
                word_dict[(2, no_vowels)] = w
                
        ans = []
        for q in queries:
            w = word_dict[(0, q)] or \
                word_dict[(1, q.lower())] or \
                word_dict[(2, "".join('.' if c in 'aeoiu' else c for c in q.lower()))]
            ans.append(w)
        return ans
# @lc code=end

