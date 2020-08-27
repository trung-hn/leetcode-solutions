#
# @lc app=leetcode id=1535 lang=python3
#
# [1535] Find the Winner of an Array Game

#

# @lc code=start
# TAGS: Array
import collections
class Solution:
    # 760 ms, 58.59%. Time and Space: O(N)
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr): return max(arr)
        arr = collections.deque(arr)
        freq = collections.defaultdict(int)
        while 1:
            if arr[0] > arr[1]:
                arr[0], arr[1] = arr[1], arr[0]
            arr.rotate(-1)
            freq[arr[0]] += 1
            if freq[arr[0]] == k: return arr[0]
    
    # Inspired from lee215 solution.
    # We make use of the fact that we only go through the array once. else, the max will win
    # 648 ms, 96.84 %. Time: O(N). Space: O(1)
    def getWinner(self, arr: List[int], k: int) -> int:
        win = 0
        winner = arr[0]
        for num in arr[1:]:
            if num > winner:
                winner = num
                win = 1
            else:
                win += 1
            if win == k: return winner
        return max(arr)

# @lc code=end

