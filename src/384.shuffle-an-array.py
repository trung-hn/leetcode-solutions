#
# @lc app=leetcode id=384 lang=python3
#
# [384] Shuffle an Array
#

# @lc code=start


class Solution:
    # 356 ms, 16.41%. Time: O(N). Space: O(N)
    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.nums = nums

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        tmp = list(self.nums)
        self.nums = []
        while tmp:
            index = random.randint(0, len(tmp) - 1)
            tmp[-1], tmp[index] = tmp[index], tmp[-1]
            self.nums.append(tmp.pop())
        return self.nums

    # article way: Fisher-Yates Algorithm
    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            idx = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[idx] = self.nums[idx], self.nums[i]
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end
