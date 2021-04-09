#
# @lc app=leetcode id=659 lang=python3
#
# [659] Split Array into Consecutive Subsequences
#

# @lc code=start
# TAGS: Heap, Greedy
# REVIEWME: Greedy


class Solution:
    # 528 ms, 78.48%. Time: O(N). Space: O(1). Greedy
    def isPossible(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        one_ele = two_ele = sequence = 0
        prev = float("-inf")
        for val, cnt in counter.items():
            # check if val = prev + 1
            if prev + 1 != val:
                if one_ele or two_ele:
                    return False
                sequence = 0

            # Not enough cnt to convert all two_ele
            if two_ele > cnt:
                return False
            # Convert all two_ele to a sequence
            cnt -= two_ele
            new_sequence = two_ele

            # Not enough cnt to convert all one_ele
            if one_ele > cnt:
                return False
            # Convert all one_ele to two_ele
            cnt -= one_ele
            two_ele = one_ele

            # Continu as many sequencec as we can
            sequence = min(sequence, cnt)
            cnt -= sequence
            sequence += new_sequence

            # Whatever left start a new one_ele
            one_ele = cnt

            prev = val

        return one_ele == two_ele == 0

    # 516 ms, 88.52%. Time: O(N). Space: O(1). Same as above but shorter logic
    def isPossible(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        one_ele = two_ele = sequence = 0
        prev = float("-inf")
        for val, cnt in counter.items():
            # check if val = prev + 1
            if prev + 1 != val:
                if one_ele or two_ele:
                    return False
                sequence = 0

            # Not enough cnt to convert all two_ele and one_ele
            if cnt < one_ele + two_ele:
                return False

            # Convert cnt to two_ele and sequence
            cnt -= two_ele + one_ele
            continued_seq = min(sequence, cnt)
            sequence = two_ele + continued_seq
            two_ele = one_ele
            one_ele = cnt - continued_seq

            prev = val

        return one_ele == two_ele == 0
# @lc code=end
