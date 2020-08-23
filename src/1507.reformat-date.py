#
# @lc app=leetcode id=1507 lang=python3
#
# [1507] Reformat Date
#

# @lc code=start
# TAGS: String
class Solution:
    # 44 ms, 42.11%. Time and Space: O(1)
    def reformatDate(self, date: str) -> str:
        Month = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
        dd, mm, yy = date.split()
        dd = dd[:-2]
        mm = Month[mm]
        return f"{yy}-{mm:02}-{dd:0>2}"
        
# @lc code=end

