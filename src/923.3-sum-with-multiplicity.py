#
# @lc app=leetcode id=923 lang=python3
#
# [923] 3Sum With Multiplicity
#

# @lc code=start
# TAGS: Two Pointers.


class Solution:
    # 84 ms,  59.77%. Time: O(N^2). Space: O(N). Where N is the number of unique numbers in arr
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7

        def get_prod(a, b, c):
            if a == b == c:
                total = 0
                cnt = counter[a]
                for i in range(cnt):
                    rest = cnt - i - 1
                    total += rest * (rest - 1) / 2
                return total
            elif a == b:
                return counter[a] * (counter[a] - 1) / 2 * counter[c]
            elif b == c:
                return counter[b] * (counter[b] - 1) / 2 * counter[a]
            elif a == c:
                return counter[a] * (counter[a] - 1) / 2 * counter[b]
            return counter[a] * counter[b] * counter[c]

        total = 0
        counter = collections.Counter(arr)
        nums = sorted(counter.keys())
        for i, a in enumerate(nums):
            if nums[i] * 3 > target:
                break
            seen = {}
            for j, b in enumerate(nums[i:], i):
                seen[target - (a + b)] = [a, b]
                if b in seen:
                    total += get_prod(*seen[b], b) % MOD
        return int(total) % MOD
# @lc code=end
