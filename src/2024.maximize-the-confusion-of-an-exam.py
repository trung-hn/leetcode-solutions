#
# @lc app=leetcode id=2024 lang=python3
#
# [2024] Maximize the Confusion of an Exam
#

# @lc code=start
# TAGS: String, Binary Search, Sliding Window, Prefix Sum
class Solution:
    # 472 ms, 51.69%. Time and Space: O(N)
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def get_optimal(answerKey, k, neg="F"):
            ans = ptr = 0
            for i, c in enumerate(answerKey):
                if c == neg:
                    while not k:
                        k += answerKey[ptr] == neg
                        ptr += 1
                    k -= 1
                ans = max(ans, i + 1 - ptr)
            return ans

        return max(get_optimal(answerKey, k, neg="F"), get_optimal(answerKey, k, neg="T"))
# @lc code=end
