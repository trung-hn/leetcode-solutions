#
# @lc app=leetcode id=1897 lang=python3
#
# [1897] Redistribute Characters to Make All Strings Equal
#

# @lc code=start
# TAGS: Hash Table, String, Couting


class Solution:
    # 80 ms, 39.51%. Time and Space: O(N)
    def makeEqual(self, words: List[str]) -> bool:
        counter = collections.Counter()
        for word in words:
            counter += collections.Counter(word)

        return all(f % len(words) == 0 for f in counter.values())
# @lc code=end
