#
# @lc app=leetcode id=2094 lang=python3
#
# [2094] Finding 3-Digit Even Numbers
#

# @lc code=start
# NOTE: This is not bruteforce.
class Solution:
    # Time and Space: O(N)
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        def valid(d1, d2, d3):
            cnt = Counter([d1, d2, d3])
            return all(v <= counter[k] for k, v in cnt.items())

        counter = Counter(digits)
        rv = []
        for d1 in range(1, 10):
            for d2 in range(10):
                for d3 in range(0, 10, 2):
                    # alternate if statement:
                    # if cnt[i] > 0 and cnt[j] > (i == j) and cnt[k] > (k == i) + (k == j):
                    if valid(d1, d2, d3):
                        rv.append(f"{d1}{d2}{d3}")
        return rv
# @lc code=end
