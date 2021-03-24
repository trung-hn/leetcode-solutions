#
# @lc app=leetcode id=870 lang=python3
#
# [870] Advantage Shuffle
#

# @lc code=start
# TAGS: Array, Greedy
import collections


class Solution:
    # 368 ms, 49.27%. First Solution Time: O(NlogN) and Space: O(N)
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

    # 344 ms, 88.09%.  Second solution. Time: O(NlogN). Space: O(N)
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A = sorted(A)
        B = sorted((val, i) for i, val in enumerate(B))
        pre = []
        post = []
        j = 0
        for a in A:
            if a > B[j][0]:
                pre.append(a)
                j += 1
            else:
                post.append(a)
        # Reconstruct A
        for a, (_, i) in zip(pre + post, B):
            A[i] = a
        return A

    # Same complexity but cleaner from lee215

    def advantageCount(self, A, B):
        A = sorted(A)
        take = collections.defaultdict(list)
        for b in sorted(B)[::-1]:
            if b < A[-1]:
                take[b].append(A.pop())
        return [(take[b] or A).pop() for b in B]
# @lc code=end
