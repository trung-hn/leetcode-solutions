#
# @lc app=leetcode id=1419 lang=python3
#
# [1419] Minimum Number of Frogs Croaking
#

# @lc code=start
# TAGS: String


class Solution:
    """
    Approach:
    Keep track of how many frogs using state machine.
    """
    # 220 ms, 59.33%. Time and Space: O(N). Space: O(1)

    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        counter = {c: 0 for c in "croa"}
        prev = {"r": "c", "o": "r", "a": "o", "k": "a"}

        total = cur = 0
        for c in croakOfFrogs:
            if c in prev and counter[prev[c]] == 0:
                return -1

            # Keep track of counter
            if c != "c":
                counter[prev[c]] -= 1
            if c != "k":
                counter[c] += 1

            # Keep track of cur and total
            if c == "c":
                cur += 1
            if c == "k":
                cur -= 1
            total = max(total, cur)
        return -1 if cur else total
# @lc code=end
