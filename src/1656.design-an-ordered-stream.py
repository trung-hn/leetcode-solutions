#
# @lc app=leetcode id=1656 lang=python3
#
# [1656] Design an Ordered Stream
#

# @lc code=start
# TAGS: Array, Design
class OrderedStream:
    # 224 ms, 46.70%. Time and Space: O(N)
    def __init__(self, n: int):
        self.s = [None] * n
        self.ptr = 0

    def insert(self, id: int, value: str) -> List[str]:
        self.s[id - 1] = value
        start = self.ptr
        while self.ptr < len(self.s) and self.s[self.ptr]:
            self.ptr += 1
        return self.s[start:self.ptr]

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
# @lc code=end

