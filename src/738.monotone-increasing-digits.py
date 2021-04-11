#
# @lc app=leetcode id=738 lang=python3
#
# [738] Monotone Increasing Digits
#

# @lc code=start
# TAGS: Greedy


class Solution:
    """
    Aproach: Find the first decrease in value. 
    That is where we reduce the number by 1 and the rest to "9"
    If there are same digits: "3444", we change the first digit of the sequence
    ptr is used to find the index of the first digit
    """

    # 28 ms, 85.49%. Time and Space: O(logN)
    def monotoneIncreasingDigits(self, N: int) -> int:
        def change_at(i):
            # Reduce val at ptr
            S[i] = str(int(S[i]) - 1)
            # Change all digits after that to '9'
            S[i + 1:] = "9" * len(S[i + 1:])

        S = list(str(N))
        ptr = 0
        for i in range(len(S) - 1):
            if S[i] > S[i + 1]:
                change_at(ptr)
                return int("".join(S))
            elif S[i] < S[i + 1]:
                ptr = i + 1
        return int("".join(S))
# @lc code=end
