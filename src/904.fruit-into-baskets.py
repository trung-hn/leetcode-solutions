#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

# @lc code=start
# TAGS: Two Pointers
class Solution:
    # 896 ms, 32.39%. Time: O(N). Space: O(1)
    def totalFruit(self, tree: List[int]) -> int:
        ans = 0; ptr = -1
        collected = collections.defaultdict(int)
        for i, fruit in enumerate(tree):
            collected[fruit] += 1
            while len(collected.keys()) > 2:
                ptr += 1
                collected[tree[ptr]] -= 1
                if collected[tree[ptr]] == 0:
                    del collected[tree[ptr]]
            ans = max(ans, i - ptr)            
        return ans
            
        
# @lc code=end

