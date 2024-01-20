#
# @lc app=leetcode id=2347 lang=python3
#
# [2347] Best Poker Hand
#

# @lc code=start
# TAGS: Array, Hash Table, Counting
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"

        counter = collections.defaultdict(int)
        for r in ranks:
            counter[r] += 1
        mx = max(counter.values())

        if mx >= 3:
            return "Three of a Kind"

        if mx == 2:
            return "Pair"
        
        return "High Card"
# @lc code=end

