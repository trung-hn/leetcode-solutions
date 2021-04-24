#
# @lc app=leetcode id=1629 lang=python3
#
# [1629] Slowest Key
#

# @lc code=start
# TAGS: Array


class Solution:
    # 56 ms, 66.95%. Time: O(N). Space: O(1)
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        result = (releaseTimes[0], keysPressed[0])
        for t1, t2, key in zip(releaseTimes, releaseTimes[1:], keysPressed[1:]):
            result = max(result, (t2 - t1, key))
        return result[1]

    # 64 ms, 35.42%. Time: O(N). Space: O(1)
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longest_key = keysPressed[0]
        longest_time = 0
        for i in range(len(releaseTimes)):
            t1 = 0 if i == 0 else releaseTimes[i - 1]
            t2 = releaseTimes[i]
            if (t2 - t1) > longest_time:
                longest_time = t2 - t1
                longest_key = keysPressed[i]
            elif (t2 - t1) == longest_time and longest_key < keysPressed[i]:
                longest_key = keysPressed[i]
        return longest_key
# @lc code=end
