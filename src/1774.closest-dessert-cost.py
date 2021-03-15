#
# @lc app=leetcode id=1774 lang=python3
#
# [1774] Closest Dessert Cost
#

# @lc code=start
# TAGS: Greedy
# REVIEWME: Dynamic Programming


class Solution:
    # 564 ms. Time: O(N*2^M). Space: O(2^M)
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        counter = [0] * len(toppingCosts)
        all_tops = set()

        def get_tops(sofar=0, start=0):
            all_tops.add(sofar)
            for i in range(start, len(toppingCosts)):
                if counter[i] == 2:
                    continue
                counter[i] += 1
                get_tops(sofar + toppingCosts[i], i)
                counter[i] -= 1

        get_tops()
        ans = float("inf")
        for base in baseCosts:
            for top in all_tops:
                if abs(base + top - target) < abs(ans - target):
                    ans = base + top
                elif abs(base + top - target) == abs(ans - target):
                    ans = min(ans, base + top)
        return ans

    # 64 ms. Time: O(N*M*V). Space: O(M*V).From discussion
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        toppingCosts *= 2

        @cache
        def fn(i, x):
            """Return sum of subsequence of toppingCosts[i:] closest to x."""
            if x < 0 or i == len(toppingCosts):
                return 0
            return min(fn(i+1, x), toppingCosts[i] + fn(i+1, x-toppingCosts[i]), key=lambda y: (abs(y-x), y))

        ans = inf
        for bc in baseCosts:
            ans = min(ans, bc + fn(0, target - bc),
                      key=lambda x: (abs(x-target), x))
        return ans


# @lc code=end
