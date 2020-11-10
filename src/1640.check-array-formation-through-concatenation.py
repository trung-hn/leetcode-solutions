#
# @lc app=leetcode id=1640 lang=python3
#
# [1640] Check Array Formation Through Concatenation
#

# @lc code=start
# TAGS: Array
class Solution:
    # 40 ms, 80.70%. Time and Space: O(N)
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        index_dict = {val:i for i, val in enumerate(arr)}
        for piece in pieces:
            if piece[0] not in index_dict: return False
            index = index_dict[piece[0]]
            if piece != arr[index : index + len(piece)]:
                return False
        return True
# @lc code=end

