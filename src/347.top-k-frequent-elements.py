#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
# TAGS: Heap, Hash Table


class Solution:
    # Time: O(NlogK). Space: O(K)
    def topKFrequent(self, nums, k):
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

    # 84 ms, 99.75% Time: O(NlogK). Space: O(K)
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        D = collections.Counter(nums)
        L = []
        for k, v in D.items():
            if len(L) < K:
                heapq.heappush(L, (v, k))
            elif v > L[0][0]:
                heapq.heapreplace(L, (v, k))
        return [f for _, f in L]

    # 96 ms, 86.32 % dict. O(N)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group_by_freq = collections.defaultdict(list)
        for num, freq in Counter(nums).items():
            group_by_freq[freq].append(num)

        ans = []
        for i in reversed(range(max(group_by_freq)+1)):
            ans.extend(group_by_freq[i])
        return ans[:k]

    # 128 ms, 26 % dict. O(Nlog(N))
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        D = collections.Counter(nums)
        return sorted(D.keys(), key=lambda k: D[k], reverse=True)[:k]
# @lc code=end
