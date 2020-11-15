#
# @lc app=leetcode id=1629 lang=python3
#
# [1629] Slowest Key
#

# @lc code=start
# TAGS: Array
class Solution:
    # 64 ms, 35.42%. Time: O(N). Space: O(1)
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longest_key = keysPressed[0]; longest_time = 0
        for i in range(len(releaseTimes)):
            t1 = 0 if i == 0 else releaseTimes[i - 1]
            t2 = releaseTimes[i]    
            if (t2 - t1) > longest_time :
                longest_time = t2 - t1
                longest_key = keysPressed[i]
            elif (t2 - t1) == longest_time and longest_key < keysPressed[i]:
                longest_key = keysPressed[i]
        return longest_key
    
    # 56 ms, 72.61%. Time and Space: O(N)
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        releaseTimes = [0] + releaseTimes
        array = ([t2 - t1, k] for t1, t2, k in zip(releaseTimes, releaseTimes[1:], keysPressed))
        return max(array)[1]
# @lc code=end

