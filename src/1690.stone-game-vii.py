#
# @lc app=leetcode id=1690 lang=python3
#
# [1690] Stone Game VII
#

# @lc code=start
# TAGS: Dynamic Programming
# REVIEWME: Dynamic Programming


class Solution:
    """
    This problem has a very tight time requirement. 
    Thus, @cache will result in LTE. 
    @lru_cache(2000) is a magic number that just works. No idea why

    Explanation about this solution: https://leetcode.com/problems/stone-game-vii/discuss/970281/C%2B%2BJavaPython-Minimax-Top-down-Bottom-up-DP-Clean-and-Concise
    Explanation about LTE errors: https://leetcode.com/problems/stone-game-vii/discuss/1264544/Python-O(n*n)-dp-solution-how-to-avoid-TLE-explained
    """
    # 5704 ms, 41.07%. Time: O(N^2). Space: O(N^2)

    def stoneGameVII(self, stones: List[int]) -> int:

        prefix_sum = [0]
        for stone in stones:
            prefix_sum.append(prefix_sum[-1] + stone)

        @lru_cache(2000)
        def dp(left, right, alice_turn):
            if left == right:
                return 0

            if alice_turn:
                # Alice gains points
                a = dp(left + 1, right, not alice_turn) + \
                    prefix_sum[right] - prefix_sum[left + 1]
                b = dp(left, right - 1, not alice_turn) + \
                    prefix_sum[right - 1] - prefix_sum[left]
                return max(a, b)
            else:
                # Bob gains points
                a = dp(left + 1, right, not alice_turn) - \
                    (prefix_sum[right] - prefix_sum[left + 1])
                b = dp(left, right - 1, not alice_turn) - \
                    (prefix_sum[right - 1] - prefix_sum[left])
                return min(a, b)
        return dp(0, len(stones), True)


# @lc code=end
