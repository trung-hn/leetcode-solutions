#
# @lc app=leetcode id=1854 lang=python3
#
# [1854] Maximum Population Year
#

# @lc code=start
# TAGS: Array, Counting


class Solution:
    # 24 ms, 100%. Time: O(NlogN). Space: O(N)
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        counter = collections.defaultdict(lambda: [0, 0])
        for s, e in logs:
            counter[s][0] += 1
            counter[e][1] += 1

        curr = 0
        max_pop = 0
        ans = 0
        for yr in sorted(counter.keys()):
            curr += counter[yr][0]
            curr -= counter[yr][1]
            if curr > max_pop:
                max_pop = curr
                ans = yr
        return ans


# @lc code=end
