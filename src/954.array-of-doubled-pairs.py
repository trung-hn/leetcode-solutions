#
# @lc app=leetcode id=954 lang=python3
#
# [954] Array of Doubled Pairs
#

# @lc code=start
# TAGS: Array, Hash Table, Greedy, Sorting


class Solution:
    # 680 ms, 63.64%. Time: O(NlogN). Space: O(N)
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort(key=abs, reverse=True)
        counter = collections.Counter()
        cnt = 0
        for num in arr:
            double = num * 2
            if counter[double]:
                counter[double] -= 1
                cnt += 1
            else:
                counter[num] += 1
        return cnt >= len(arr) / 2
# @lc code=end
