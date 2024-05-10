#
# @lc app=leetcode id=2502 lang=python3
#
# [2502] Design Memory Allocator
#


# @lc code=start
# TAGS: Array, Hash Table, Design, Simulation
class Allocator:
    """
    `self.mem` only stores how many memory space is occupied from current index.
    Example:
    [3, 0, 0, 0] means only the last space is empty.

    This improves `allocate()` because we can directly jump to the next empty index.
    This improves `free()` because we only modify the first index.

    This solution is still not optimal.
    """

    def __init__(self, n: int):
        self.mem = [0] * n
        self.tracker = collections.defaultdict(set)

    def allocate(self, size: int, mID: int) -> int:
        cnt = i = 0
        while i < len(self.mem):
            if self.mem[i]:
                cnt = 0
                i += self.mem[i]
            else:
                cnt += 1
                i += 1
            if cnt == size:
                self.tracker[mID].add(i - size)
                self.mem[i - size] = size
                return i - size
        return -1

    def free(self, mID: int) -> int:
        ans = 0
        for i in self.tracker[mID]:
            ans += self.mem[i]
            self.mem[i] = 0
        del self.tracker[mID]
        return ans


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
# @lc code=end
