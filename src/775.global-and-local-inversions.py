#
# @lc app=leetcode id=775 lang=python3
#
# [775] Global and Local Inversions
#

# @lc code=start
# TAGS: Array, Math


class Solution:
    # Time and Space: O(N)
    def isIdealPermutation(self, A: List[int]) -> bool:
        pos = {v: i for i, v in enumerate(A)}
        for v1, v2 in zip(A, A[1:]):
            if v1 < v2:
                continue

            # diff > 1
            if v1 != v2 + 1:
                return False

            # 3 has to appear after 2
            if (v1 + 1) in pos and pos[v1 + 1] < pos[v1]:
                return False

            # 1 has to appear before 2
            if (v2 - 1) in pos and pos[v2 - 1] > pos[v2]:
                return False
        return True

    # 320 ms, 95.02%. Time: O(N). Space: O(1)
    # need intuition to come to this solution, looks at lee215 post
    def isIdealPermutation(self, A: List[int]) -> bool:
        return all(abs(val - i) <= 1 for i, val in enumerate(A))
# @lc code=end
