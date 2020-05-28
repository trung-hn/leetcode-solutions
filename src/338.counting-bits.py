#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
# TAGS: Dynamic Programming, Bit Manipulation
# REVIEWME: There are good solutions in the article
class Solution:
    # 104 ms, 46%. Not as good
    def countBits(self, num: int) -> List[int]:
        return [str(bin(n)).count("1") for n in range(num+1)]
    
    # 92 ms, 87%. Time and Space: O(N)
    # Bit shifting solution
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        for n in range(1, num+1):
            ans.append(ans[n // 2] + n % 2)
            # ans.append(ans[n >> 2] + n ^ 1)
        return ans
    
    # 68 ms, 99.55%. Time and Space: O(N)
    def countBits(self, num: int) -> List[int]:
        power_of_two = set(2**i for i in range(32))
        ans = [0]
        ptr = 0
        for i in range(1, num + 1):
            if i in power_of_two:
                ans.append(1)
                ptr = i
            else:
                ans.append(ans[ptr] + ans[i - ptr])
        return ans
# @lc code=end

