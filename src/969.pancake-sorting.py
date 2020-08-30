#
# @lc app=leetcode id=969 lang=python3
#
# [969] Pancake Sorting
#

# @lc code=start
# TAGS: Array
class Solution:
    # Very Weird Problem
    # 44 ms, 70 %. Time: O(N^2). Space: O(N). This is bubble sort. 
    def pancakeSort(self, A: List[int]) -> List[int]:
        def flip(index):
            half = index // 2
            for i in range(half + 1):
                A[i], A[index - i] = A[index - i], A[i]
                
        ans = []
        N = len(A)
        for val in reversed(range(1, N + 1)):
            max_arg = A.index(val)

            ans.append(max_arg + 1)
            flip(max_arg)

            ans.append(val)
            flip(val - 1)
        return ans

        
# @lc code=end
