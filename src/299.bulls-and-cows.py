#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
# TAGS: Hash Table
import collections
class Solution:
    # 36 ms, 91.56 %. Time and Space: O(N), N is the length of the number
    def getHint(self, secret: str, guess: str) -> str:
        bull = cow = 0
        counter = collections.Counter(secret)
        for d1, d2 in zip(secret, guess):
            if d1 == d2:
                counter[d2] -= 1
                bull += 1

        for d1, d2 in zip(secret, guess):
            if d1 != d2 and counter[d2] > 0:
                counter[d2] -= 1
                cow += 1
        return f"{bull}A{cow}B"

    # Pythonic. 
    # 36 ms, 91.56 %. Time and Space: O(N), N is the length of the number
    def getHint(self, secret: str, guess: str) -> str:
        bull = sum(a == b for a, b in zip(secret, guess))
        cow = collections.Counter(secret) & collections.Counter(guess) # intersection (set op)
        return f"{bull}A{sum(cow.values()) - bull}B"

# @lc code=end

