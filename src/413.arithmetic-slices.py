#
# @lc app=leetcode id=413 lang=python3
#
# [413] Arithmetic Slices
#

# @lc code=start
# TAGS: Math, Dynamic Programming
class Solution:
    # 32 ms, 91.35%. Time: O(N). Space: O(1)
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        A += [float("inf")]
        def get_count(length):
            return (length + 1) * length // 2
        
        sequence = False
        ptr = total = 0
        for i in range(2, len(A)):
            n1, n2, n3 = A[i - 2: i+1]
            if n3 - n2 == n2 - n1:
                if not sequence:
                    ptr = i
                sequence = True
            elif sequence:
                total += get_count(i - ptr)
                sequence = False
        return total
# @lc code=end

