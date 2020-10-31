# TAGS: Hash Table, Array, Premium
class Solution:
    # LTE. Time: O(M^2)
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = 0
        arrays = [[arr[0], arr[-1]] for arr in arrays]
        for i, (minval, _) in enumerate(arrays):
            for j, (_, maxval) in enumerate(arrays):
                if j == i: continue
                ans = max(ans, abs(maxval - minval))
        return ans
    
    # 160 ms, 93.83%. Time: O(NlogN). Space: O(N)
    def maxDistance(self, arrays: List[List[int]]) -> int:
        nums = []
        arrays = [[arr[0], arr[-1]] for arr in arrays]
        for i, (minval, maxval) in enumerate(arrays):
            nums.append((minval, i))
            nums.append((maxval, i))
        nums.sort()
        
        ans = 0        
        N = len(nums) - 1
        for start, end in (0, N), (0, N - 1), (1, N), (1, N - 1):
            if nums[start][1] == nums[end][1]: continue
            ans = max(ans, nums[end][0] - nums[start][0])
        return ans
    
    # 168 ms, 83.26%. Time: O(N). Space: O(1)
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest = arrays[0][0]
        largest = arrays[0][-1]
        ans = 0
        for array in arrays[1:]:
            min_val, max_val = array[0], array[-1]
            ans = max([ans, max_val - smallest, largest - min_val])
            smallest = min(smallest, min_val)
            largest = max(largest, max_val)
        return ans
            
    