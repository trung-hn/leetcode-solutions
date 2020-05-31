#
# @lc app=leetcode id=1442 lang=python3
#
# [1442] Count Triplets That Can Form Two Arrays of Equal XOR
#

# @lc code=start
# TAGS: Array, Math, Bit Manipulation
# REVIEWME: The bit manipulation aspect of this problem is mind blowing . 
class Solution:
    """
    There are 3 solutions below with different complexity
    ref: https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/discuss/623747/JavaC%2B%2BPython-One-Pass-O(N4)-to-O(N)
    There is even a 1 pass solution which mean we perform both step in the same loop.
    """
    # 5816 ms, 16.07%. Time: O(N^3). Space O(N)
    def countTriplets(self, arr: List[int]) -> int:
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] ^ num)
        
        cnt = 0
        for i in range(1, len(prefix)):
            for j in range(i + 1, len(prefix)):
                for k in range(j, len(prefix)):
                    a = prefix[i - 1] ^ prefix[j - 1]
                    b = prefix[k] ^ prefix[j - 1]
                    if a == b:
                        cnt += 1
        return cnt
    
    # Because a ^ b == 0 => range(i, j, k) xor each other == 0 => prefix[i] = prefix[k + 1]
    # 52 ms, 81.22%. Time: O(N^2). Space O(N)
    def countTriplets(self, arr: List[int]) -> int:
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] ^ num)
        
        cnt = 0
        for i in range(0, len(prefix)):
            for k in range(i + 1, len(prefix)):
                if prefix[i] == prefix[k]:
                    cnt += k - i - 1
        return cnt

    # Refer to the post for explanation
    # 32 ms, 96%. Time: O(N). Space O(N)
    # (i - i1 - 1) + (i - i2 - 1) + (i - i3 - 1)
    # = f * i - (i1 + i2 + i3) - f 
    # = (i - 1) * f - (i1 + i2 + i3)
    # f is number of time same number occurred
    def countTriplets(self, arr: List[int]) -> int:
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] ^ num)
        
        cnt = 0
        C = collections.Counter()
        T = collections.Counter()
        for i in range(0, len(prefix)):
            cnt += C[prefix[i]] * (i - 1) - T[prefix[i]]
            C[prefix[i]] += 1
            T[prefix[i]] += i
        return cnt

# @lc code=end

