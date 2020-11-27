# TAGS: Premium, Hash Table, Two Pointers, String, Sliding Window

class Solution:
    # 360 ms, 5.36%. Time: O(N). Space; O(1)
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        def valid(counter):
            return len(list(v for v, f in counter.items() if f > 0)) <= 2
        
        counter = collections.Counter()
        left = ans = 0
        for right, c in enumerate(s):
            counter[c] += 1
            if not valid(counter):
                while not valid(counter):
                    counter[s[left]] -= 1
                    left += 1
            ans = max(ans, right - left + 1)
        return ans
    
    # 40 ms, 98.59%. Time: O(N). Space; O(1)
    def lengthOfLongestSubstringTwoDistinct1(self, s: str) -> int:
        counter = {}
        left = ans = 0
        for right, c in enumerate(s):
            counter[c] = right
            if len(counter) > 2:
                left = min(counter.values())
                del counter[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans