#
# @lc app=leetcode id=948 lang=python3
#
# [948] Bag of Tokens
#

# @lc code=start
# TAGS: Greedy
import collections
class Solution:
    # 52 ms, 74.54%. 2 pointers. Time: O(NlogN). Space: O(N)
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        lo, hi = 0, len(tokens) - 1
        score = max_score = 0
        power = P
        while lo <= hi:
            if power >= tokens[lo]:
                power -= tokens[lo]
                score += 1
                lo += 1
            elif score:
                power += tokens[hi]
                score -= 1
                hi -= 1
            else:
                break
            max_score = max(max_score, score)
        return max_score

    # 56 ms, 47.23%. Deque. Time: O(NlogN). Space: O(N)
    def bagOfTokensScore1(self, tokens: List[int], P: int) -> int:
        deque = collections.deque(sorted(tokens))
        score = max_score = 0
        power = P
        while deque and (deque[0] <= power or score):
            if deque[0] <= power:
                power -= deque.popleft()
                score += 1
            elif score:
                power += deque.pop()
                score -= 1
            max_score = max(max_score, score)
        return max_score

# @lc code=end

