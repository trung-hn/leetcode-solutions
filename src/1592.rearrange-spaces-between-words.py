#
# @lc app=leetcode id=1592 lang=python3
#
# [1592] Rearrange Spaces Between Words
#

# @lc code=start
# TAGS: String
class Solution:
    # 24 ms, 94.72%. Time: O(N). Space: O(N)
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(' ')
        words = text.split()
        if len(words) == 1: 
            return words[0] + ' ' * spaces
        div, rem = divmod(spaces, len(words) - 1)
        delimiter = ' ' * div
        return delimiter.join(words) + ' ' * rem
        
# @lc code=end

