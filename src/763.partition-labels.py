#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
# TAGS: Greedy, Two Pointers
# REVIEWME: Greedy 
class Solution:
    # 20 ms, 99%. Time and Space: O(N)
    def partitionLabels(self, S: str) -> List[int]:
        alpha = [None]*26
        # Get first and last appearance
        for i, c in enumerate(S):
            pos = ord(c) - ord('a')
            if alpha[pos] is None:
                alpha[pos] = [i, i+1]
            else:
                alpha[pos][-1] = i+1

        # Sort and combine ranges.
        alpha = sorted(val for val in alpha if val)
        rv = [alpha[0][1] - alpha[0][0]]
        for i in range(1, len(alpha)):
            if alpha[i][0] < alpha[i-1][1]:
                alpha[i][0] = alpha[i-1][0]
                alpha[i][1] = max(alpha[i-1][1], alpha[i][1])
                rv.pop()
            rv.append(alpha[i][1] - alpha[i][0])
        return rv

    # 36 ms, 75%. Time and Space: O(N) using ordered dict
    def partitionLabels(self, S: str) -> List[int]:
        alpha = collections.OrderedDict()
        # Get first and last appearance
        for i, c in enumerate(S):
            if c not in alpha:
                alpha[c] = [i, i+1]
            else:
                alpha[c][-1] = i+1
        alpha = list(alpha.values())
    
        rv = [alpha[0][1] - alpha[0][0]]
        for i in range(1, len(alpha)):
            if alpha[i][0] < alpha[i-1][1]:
                alpha[i][0] = alpha[i-1][0]
                alpha[i][1] = max(alpha[i-1][1], alpha[i][1])
                rv.pop()
            rv.append(alpha[i][1] - alpha[i][0])
        return rv
    
    # 36 ms, 75.51% Greedy. Time and space: O(N)
    def partitionLabels(self, S: str) -> List[int]:
        # read solution article for explanation
        last = {c:i for i, c in enumerate(S)}
        end = start = 0
        ans = []
        for i, c in enumerate(S):
            end = max(end, last[c])
            if end == i:
                ans.append(end - start + 1)
                start = i + 1
        return ans
            
            
# @lc code=end

