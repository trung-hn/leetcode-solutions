# TAGS: Array, Premium
class Solution:
    # 64 ms, 15.55%. O(N), O(N)
    def countElements(self, arr: List[int]) -> int:
        seen = set(arr)
        return sum(1 for val in arr if val + 1 in seen)