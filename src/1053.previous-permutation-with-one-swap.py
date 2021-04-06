#
# @lc app=leetcode id=1053 lang=python3
#
# [1053] Previous Permutation With One Swap
#

# @lc code=start
# TAGS: Array, Greedy


class Solution:
    # The bigger value should be as far right as possible
    # The smaller value should be the next smaller value (that is to the right of bigger value)
    # If there are multiple smaller values, pick the one nearest to the bigger value.
    # 224 ms, 87.42%. Time: O(N). Space: O(1)
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        def swap_at(i, seen):
            for j in reversed(range(1, arr[i])):
                if j not in seen:
                    continue
                arr[i], arr[seen[j]] = arr[seen[j]], arr[i]
                return

        seen = {}
        for i in reversed(range(len(arr))):
            if seen and arr[i] > min(seen):
                swap_at(i, seen)
                break
            seen[arr[i]] = i
        return arr
# @lc code=end
