#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
# TAGS: String, Backtracking, DFS, Recursion


class Solution:
    # 32 ms, 54.64%. Time and Space: O(2^N)
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        chars = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                 "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        queue = [""]
        for d in digits:
            nxt = []
            for c in chars[d]:
                for s in queue:
                    nxt.append(s + c)
            queue = nxt
        return queue
# @lc code=end
