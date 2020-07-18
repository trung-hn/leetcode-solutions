#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
# TAGS: Heap, Hash Table
class Solution:
    
    def topKFrequent(self, nums, k):
        count = collections.Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get) 
    
    # 116 ms, 84% O(Nlog(K))
    def topKFrequent1(self, nums: List[int], K: int) -> List[int]:
        D = collections.Counter(nums)
        L = []
        for k, v in D.items():
            if len(L)<K:
                heapq.heappush(L, (v, k))
            elif v > L[0][0]:
                heapq.heapreplace(L, (v, k))
        ans = []
        while(L):
            ans.append(heapq.heappop(L)[1])
        return ans
        
    # 116 ms, 84 % dict. O(N). Bucketing
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter, defaultdict
        D = defaultdict(list)
        for key, v in Counter(nums).items():
            D[v].append(key)
        ans = []
        for i in reversed(range(max(D)+1)):
            ans.extend(D[i])
        return ans[:k]
        
    # 128 ms, 26 % dict. O(Nlog(N))
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        D = collections.Counter(nums)
        return sorted(D.keys(), key=lambda k: D[k], reverse = True)[:k]
# @lc code=end

