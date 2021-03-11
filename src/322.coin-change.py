#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
# TAGS: Dynamic Programming


class Solution:
    # 1240 ms, 77%. bfs with memoization. Time and Space: O(A*N)
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        visited = set()
        q = [(amount, 1)]
        for amount, step in q:
            if amount in visited:
                continue
            visited.add(amount)
            for coin in coins:
                if coin == amount:
                    return step
                if coin < amount:
                    q.append((amount - coin, step + 1))
        return -1

    # 1264 ms, 64.18%. Time: O(A*N), space: O(A). DP solution
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        dp = [0] + [float("inf")]*amount
        for coin in coins:
            for i in range(coin, amount + 1):
                if coin == i:
                    dp[i] = 1
                else:
                    dp[i] = min(dp[i], dp[i - coin] + dp[coin])
        return dp[amount] if dp[amount] <= amount else -1

    # 660 ms, 94.18%. Time: O(A*N). Space: O(A). A is the amount, N is number of coins
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        ans = 0
        visited = set()
        q = [amount]
        while q:
            ans += 1
            nxt = set()
            for amt in q:
                if amt in visited:
                    continue
                visited.add(amt)
                for coin in coins:
                    if coin == amt:
                        return ans
                    if coin < amt:
                        nxt.add(amt - coin)
            q = nxt
        return -1
# @lc code=end
