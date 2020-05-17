# REVIEWME:
class Solution:
    # 32 ms, 61.03%. Time: O(N + S), Space: O(1)
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        index = 0
        for dr, amnt in shift:
            index += amnt if dr == 0 else -amnt
        index %= len(s)
        return s[index:] + s[:index]