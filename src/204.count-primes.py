#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
# TAGS: Hash Table, Math


class Solution:
    """
    Time: O(loglogN)
    Space: O(N)
    """

    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [True] * n
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False
        return sum(primes) - 2

    # 304 ms, 91.39%. Slighly more optimized when we ignore even numbers.
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        def count_primes(n):

            # Generate [0,1,0,1,0,1,...].
            # Note: with this generation, 1 is prime and 2 is not prime. But I return sum of 1s, so it does not matter much
            primes = [False, True] * (n//2)
            if n % 2:
                primes += [False]

            for i in range(3, int(n**0.5) + 1, 2):
                if primes[i]:
                    primes[i*i:n:i] = [False] * int((n-i*i-1)/i + 1)
            return sum(primes)
        return count_primes(n)
# @lc code=end
