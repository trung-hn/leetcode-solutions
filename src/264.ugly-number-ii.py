#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#

# @lc code=start
# TAGS: Heap, Dynamic Programming
class Solution:
    # 228 ms, 40.92%. Using Heap. Time and Space: O(1)
    def nthUglyNumber(self, n: int) -> int:
        numbers = [1]
        seen = set(numbers)
        for _ in range(n - 1):
            min_val = heapq.heappop(numbers)
            for val in (2, 3, 5):
                new_val = val * min_val
                if new_val not in seen:
                    seen.add(new_val)
                    heapq.heappush(numbers, new_val)
        return heapq.heappop(numbers)

    # 188 ms, 54.85%. Dynamic Programming. Time and Space: O(1)
    def nthUglyNumber(self, n: int) -> int:
        numbers = [1]
        i2 = i3 = i5 = 0
        while len(numbers) < n:
            min_val = min(numbers[i2] * 2, numbers[i3] * 3, numbers[i5] * 5)
            numbers.append(min_val)
            if min_val == numbers[i2] * 2:
                i2 += 1
            if min_val == numbers[i3] * 3:
                i3 += 1
            if min_val == numbers[i5] * 5:
                i5 += 1
        return numbers[-1]
        
# @lc code=end

