#
# @lc app=leetcode id=1769 lang=python3
#
# [1769] Minimum Number of Operations to Move All Balls to Each Box
#

# @lc code=start
# TAGS: Array, Greedy


class Solution:
    # 72 ms. Time and Space: O(N)
    def minOperations(self, boxes: str) -> List[int]:
        prefix = [0]
        for box in boxes:
            prefix.append(prefix[-1] + 1 if box == '1' else prefix[-1])

        suffix = [prefix[-1]]
        for box in boxes:
            suffix.append(suffix[-1] - 1 if box == '1' else suffix[-1])

        init = sum(i for i, b in enumerate(boxes) if b == '1')
        ans = [init]
        for pre, suf in zip(prefix[1:-1], suffix[1:-1]):
            ans.append(ans[-1] + pre - suf)
        return ans

    # 60 ms Time: O(N). Space: O(1). Similar to above but less space
    def minOperations(self, boxes: str) -> List[int]:
        init = sum(i for i, b in enumerate(boxes) if b == '1')
        ans = [init]
        pre = 0
        suf = sum(b == '1' for b in boxes)
        for i, b in enumerate(boxes[:-1]):
            if b == '1':
                pre += 1
                suf -= 1
            ans.append(ans[-1] + pre - suf)
        return ans
# @lc code=end
