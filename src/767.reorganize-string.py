#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
# TAGS: String, Heap, Greedy, Sort
# REVIEWME: Heap, Greedy
import queue, collections
class Solution:
    # Greedy Priority Queue. Time: O(NlogN). Space: O(N)
    def reorganizeString(self, S: str) -> str:
        q = queue.PriorityQueue()
        for char, freq in collections.Counter(S).items():
            q.put((-freq, char))
        
        ans = [""]
        while not q.empty():
            freq, char = q.get()
            if q.empty() and char == ans[-1]: return ''
            if char == ans[-1]:
                temp = q.get()
                q.put((freq, char))
                freq, char = temp
                
            ans.append(char)
            freq += 1
            if freq: q.put((freq, char))
        
        return "".join(ans)
    
    # Greedy Heap. 24 ms, 97.44%. Time: O(NlogN). Space: O(N)
    def reorganizeString(self, S: str) -> str:
        heap = []
        for char, freq in collections.Counter(S).items():
            heapq.heappush(heap, (-freq, char))
        
        ans = [""]
        while heap:
            if len(heap) == 1 and heap[0][1] == ans[-1]: 
                return ''
            
            freq, char = heapq.heappop(heap)
            if char == ans[-1]:
                freq, char = heapq.heapreplace(heap, (freq, char))
            ans.append(char)
            
            if freq < -1: 
                heapq.heappush(heap, (freq + 1, char))
        return "".join(ans)
# @lc code=end

