#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
# TAGS: Hash Table, Sorting, Pythonic, Bucket Sort
# REVIEWME:
class Solution:
    # 40 ms, 94 %. O(N logN) because of sorting. Space: O(N)
    def frequencySort(self, s: str) -> str:        
        D = collections.Counter(s)
        ans = [k*D[k] for k in sorted(D, key=lambda k: -D[k])]
        # or
        ans = [k*D[k] for k in sorted(D, key=D.get, reverse=True)]
        return "".join(ans)
        
    # 36 ms, 96%. Pythonic solution
    def frequencySort(self, s: str) -> str:
        return "".join(k*v for k, v in collections.Counter(s).most_common())
        
    # 92 ms, 11.55% Bucket Sort. Time and Space: O(N)
    def frequencySort(self, s: str) -> str:
        if not s: return s

        C = collections.Counter(s)
        max_freq = max(C.values())

        buckets = [[] for _ in range(len(s) + 1)]

        for letter, counter  in C.items():
            buckets[counter].append(letter)
        
        return "".join(c * i for i in reversed(range(len(buckets))) for c in buckets[i])

# @lc code=end

