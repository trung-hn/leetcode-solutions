#
# @lc app=leetcode id=970 lang=python3
#
# [970] Powerful Integers
#

# @lc code=start
# TAGS: Hash Table, Math


class Solution:
    # 32 ms, 69.17%. Time: O(logx*logy). Space: O(logx+logy)
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        powers_x = set(x**i for i in range(21) if x**i <= bound)
        powers_y = set(y**i for i in range(21) if y**i <= bound)
        answer = set()
        for xi in powers_x:
            for yi in powers_y:
                if xi + yi <= bound:
                    answer.add(xi + yi)
        return answer
# @lc code=end
