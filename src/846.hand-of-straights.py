#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
# TAGS: Ordered Map
class Solution:
    # 152 ms,  99.95%. Time: O(MlogM+NW). Space: O(N). N is unique number. M is len(hand)
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        counter = collections.Counter(hand)
        for curr in sorted(counter):
            quantity = counter[curr]
            if quantity <= 0: continue
            for i in range(curr, curr + W):
                if counter[i] < quantity: return False
                counter[i] -= quantity
        return True
                
# @lc code=end

