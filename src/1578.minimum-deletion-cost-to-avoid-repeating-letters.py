#
# @lc app=leetcode id=1578 lang=python3
#
# [1578] Minimum Deletion Cost to Avoid Repeating Letters
#

# @lc code=start
# TAGS: Greedy
class Solution:
    # 1128 ms, 93.65%. Time: O(N). Space: O(1)
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = i = 0
        while i < len(s) - 1:
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                j += 1
            ans += sum(cost[i : j]) - max(cost[i : j])
            i = j
        return ans

    # 1184 ms, 81.52 %. Similar as above but slightly different. 
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = 0
        max_cost = cost[0]
        total = cost[0]
        for i in range(len(s)):
            if i == len(s) - 1:
                ans += total - max_cost
                break
            if s[i] == s[i + 1]:
                max_cost = max(max_cost, cost[i + 1])
                total += cost[i + 1]
            else:
                ans += total - max_cost
                total = cost[i + 1]
                max_cost = cost[i + 1]
        return ans

# @lc code=end

