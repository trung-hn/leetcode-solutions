#
# @lc app=leetcode id=870 lang=python3
#
# [870] Advantage Shuffle
#

# @lc code=start
# TAGS: Array, Greedy
class Solution:
    # 368 ms, 49.27%. Time: O(NlogN) and Space: O(N)
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        a = list(reversed(sorted(A)))
        b = list(reversed(sorted(B)))
        
        # Find As that can be used to cover Bs
        relation = collections.defaultdict(list)
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] > b[j]:
                relation[b[j]].append(a[i])
                i += 1
            j += 1
        
        # Create the rv array
        ans = []
        for val in B:
            if relation[val]:
                ans.append(relation[val].pop())
            else:
                ans.append(a[i])
                i += 1
        return ans
# @lc code=end

