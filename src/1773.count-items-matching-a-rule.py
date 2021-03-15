#
# @lc app=leetcode id=1773 lang=python3
#
# [1773] Count Items Matching a Rule
#

# @lc code=start
# TAGS: Array, String


class Solution:
    # 240 ms, 100%. Time: O(N). Space: O(1)
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        pos = {"type": 0, "color": 1, "name": 2}
        return sum(item[pos[ruleKey]] == ruleValue for item in items)
# @lc code=end
