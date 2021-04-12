#
# @lc app=leetcode id=667 lang=python3
#
# [667] Beautiful Arrangement II
#

# @lc code=start
# TAGS: Array


class Solution:
    """
    Greedily construct the array:
    1 2 3 4
     7 6 5 
    """
    # 44 ms, 86.00 %. Time and Space: O(N)

    def constructArray(self, n: int, k: int) -> List[int]:
        lo = 1
        hi = lo + k
        output = []
        while lo <= hi:
            output.append(lo)
            if hi != lo:
                output.append(hi)
            lo += 1
            hi -= 1
        return output + list(range(k + 2, n + 1))
# @lc code=end
