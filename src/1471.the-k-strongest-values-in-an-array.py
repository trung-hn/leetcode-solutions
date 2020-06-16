#
# @lc app=leetcode id=1471 lang=python3
#
# [1471] The k Strongest Values in an Array
#

# @lc code=start
# TAGS: Sort, Array
class Solution:
    """
    There is a better solution using Quick Select
    https://leetcode.com/problems/the-k-strongest-values-in-an-array/discuss/674346/Learn-randomized-algorithm-today-which-solves-this-problem-in-O(n).
    """
    # 1116 ms, 86.47%. Custom Sort. O(NlogN). Space: O(1) best case, O(N) worst case due to sorting.
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        def custom_sort(a):
            diff_a = abs(a - median)
            return (diff_a, a)
            
        arr.sort()
        median = arr[(len(arr) - 1) // 2]
        
        arr.sort(key=custom_sort)
        return arr[-k:]

# @lc code=end

