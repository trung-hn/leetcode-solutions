#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
class Solution:
    # 80 ms, 50.80%. Time: O(N). Space: O(N). Could be better using Bit manipulation to make it O(1) Space
    # More here: https://leetcode.com/problems/shuffle-the-array/discuss/675956/In-Place-O(n)-Time-O(1)-Space-With-Explanation-and-Analysis
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i + n])
        return ans
# @lc code=end

