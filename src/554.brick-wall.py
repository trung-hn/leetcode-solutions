#
# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#

# @lc code=start
# TAGS: Hash Table


class Solution:
    """
    Approach: Count Prefix sum
    """
    # 176 ms, 84.56 %. Time and Space: O(N). N is number of total bricks

    def leastBricks(self, wall: List[List[int]]) -> int:
        counter = collections.defaultdict(int)
        for row in wall:
            prefix = 0
            for brick in row[:-1]:
                prefix += brick
                counter[prefix] += 1
        if not counter:
            return len(wall)
        return len(wall) - max(counter.values())
# @lc code=end
