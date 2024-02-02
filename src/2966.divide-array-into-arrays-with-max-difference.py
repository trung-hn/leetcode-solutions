#
# @lc app=leetcode id=2966 lang=python3
#
# [2966] Divide Array Into Arrays With Max Difference
#


# @lc code=start
# TAGS: Array, Greedy, Sorting
class Solution:
    # 708 ms, 93.43%.
    # Time: O(NlogN). Space: O(N)
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        cur = []
        for num in nums:
            if len(cur) == 3:
                ans.append(cur)
                cur = [num]
            elif len(cur) == 0:
                cur = [num]
            elif num - cur[0] <= k:
                cur.append(num)
            else:
                return []
        ans.append(cur)
        return ans


# @lc code=end
