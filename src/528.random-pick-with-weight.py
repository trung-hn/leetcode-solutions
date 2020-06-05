#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#

# @lc code=start
# TAGS: Binary Search, Random
class Solution:
    # 228 ms, 92.45%. Pythonic solution

    # O(N)
    def __init__(self, w: List[int]):
        self.nums = list(itertools.accumulate(w, operator.add))

    # O(logN)
    def pickIndex(self) -> int:
        num = random.randint(1, self.nums[-1])
        return bisect.bisect_left(self.nums, num)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

