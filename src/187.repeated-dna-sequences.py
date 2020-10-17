#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
# TAGS: Hash Table, Bit Manipulation
class Solution:
    # Bruteforce. Time and SpaceL O((N - L)*L) = O(N) where L = 10
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counter = collections.defaultdict(int)
        for i in range(len(s) - 9):
            counter[s[i : i + 10]] += 1
        return [string for string, freq in counter.items() if freq > 1]


    # from article. Rolling hash. Time and Space: O(N - L)
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)
        if n <= L:
            return []
        
        # rolling hash parameters: base a
        a = 4
        aL = pow(a, L) 
        
        # convert string to array of integers
        to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [to_int.get(s[i]) for i in range(n)]
        
        h = 0
        seen, output = set(), set()
        # iterate over all sequences of length L
        for start in range(n - L + 1):
            # compute hash of the current sequence in O(1) time
            if start != 0:
                h = h * a - nums[start - 1] * aL + nums[start + L - 1]
            # compute hash of the first sequence in O(L) time
            else:
                for i in range(L):
                    h = h * a + nums[i]
            # update output and hashset of seen sequences
            if h in seen:
                output.add(s[start:start + L])
            seen.add(h)
        return output
# @lc code=end

