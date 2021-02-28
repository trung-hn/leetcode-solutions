#
# @lc app=leetcode id=895 lang=python3
#
# [895] Maximum Frequency Stack
#

# @lc code=start
# TAGS: Hash Table, Stack
# REVIEWME: Design
import collections


class FreqStack:

    def __init__(self):
        self.counter = collections.Counter()
        self.group = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, x: int) -> None:
        self.counter[x] += 1
        self.max_freq = max(self.max_freq, self.counter[x])
        self.group[self.counter[x]].append(x)

    def pop(self) -> int:
        rv = self.group[self.max_freq].pop()
        self.counter[rv] -= 1
        if self.group[self.max_freq] == []:
            self.max_freq -= 1
        return rv

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
# @lc code=end
