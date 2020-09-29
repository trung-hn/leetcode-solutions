#
# @lc app=leetcode id=1566 lang=python3
#
# [1566] Detect Pattern of Length M Repeated K or More Times
#

# @lc code=start
# TAGS: Array
# REVIEWME: Optimal Solution. 
import collections
class Solution:
    # 36 ms, 82.36%. Time: O(N*M*K) Space: O(M)
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        if m * k > len(arr): return False
        def is_repeated(i, m, k):
            cnt = 1
            base = arr[i : i + m]
            j = i
            while j < len(arr) - m:
                j += m 
                if arr[j : j + m] == base:
                    cnt += 1
                    if cnt == k:
                        return True
                else:
                    return False

        for i in range(len(arr) - m):
            rv = is_repeated(i, m, k)
            if rv: return True
        return False
    
    # Amazing solution from discussion. Time: O(N). Space: O(1)
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        streak = 0
        for i in range(len(arr)-m):
            streak = streak + 1 if arr[i] == arr[i+m] else 0
            if streak == (k - 1) * m: return True
        return False

# @lc code=end

