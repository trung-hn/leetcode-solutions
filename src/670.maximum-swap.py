#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
# TAGS: Array, Math


class Solution:
    # 32 ms, 50.12%. Time: O(N). Space: O(N)
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))

        # Find index of largest number behind current index
        largest_behind = [""] * len(num)
        ptr = None
        for i in reversed(range(len(num))):
            largest_behind[i] = ptr
            if not ptr or num[ptr] < num[i]:
                ptr = i

        # Find first index with larger number behind exist
        for i, (n, j) in enumerate(zip(num, largest_behind[:-1])):
            if n < num[j]:
                num[i], num[j] = num[j], num[i]
                break

        return "".join(num)  # @lc code=end
