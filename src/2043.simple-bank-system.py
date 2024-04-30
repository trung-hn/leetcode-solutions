#
# @lc app=leetcode id=2043 lang=python3
#
# [2043] Simple Bank System
#

# @lc code=start
# TAGS: Array, Hash Table, Design, Simulation

from typing import List


class Bank:
    # 752 ms, 67.70%.
    def __init__(self, balance: List[int]):
        self.balance = balance

    def valid(self, i):
        return 0 < i <= len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            self.valid(account1)
            and self.valid(account2)
            and self.balance[account1 - 1] >= money
        ):
            self.withdraw(account1, money)
            self.deposit(account2, money)
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self.valid(account):
            self.balance[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.valid(account) and self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
# @lc code=end
