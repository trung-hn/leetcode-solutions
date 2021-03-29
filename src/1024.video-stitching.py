#
# @lc app=leetcode id=1024 lang=python3
#
# [1024] Video Stitching
#

# @lc code=start
# TAGS: Dynamic Programming,
# REVIEWME: Dynamic Programming,


class Solution:
    # 32 ms, 85.04% Time: O(NlogN). Space: O(1).
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        if T == 0:
            return 0
        clips.sort(key=lambda x: (x[0], -x[1]))

        if clips[0][0] > 0:
            return - 1
        n_clip = 1
        cur = clips[0][1]
        prev = -1
        for new_s, new_e in clips[1:]:
            if cur >= T or new_s > cur:
                break
            if new_s > prev:
                n_clip += 1
                prev = cur
            cur = max(cur, new_e)
        return n_clip if cur >= T else -1

# @lc code=end
