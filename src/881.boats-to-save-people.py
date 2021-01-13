#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
# TAGS: Two Pointers, Greedy
class Solution:
    # 448 ms, 74.18%. Time : O(NlogN). Space: O(N) because of sort
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0; right = len(people) - 1
        cnt = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            cnt += 1
        return cnt
# @lc code=end

