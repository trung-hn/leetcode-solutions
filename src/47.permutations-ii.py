#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
# TAGS: Backtracking
# REVIEWME: Generators
class Solution:
    # 60 ms, 60%. Pythonic
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(itertools.permutations(nums))
    
    # 148 ms, 26.58%
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def all_perms(elements):
            if len(elements) <=1:
                yield elements
            else:
                for perm in all_perms(elements[1:]):
                    for i in range(len(elements)):
                        yield perm[:i] + elements[0:1] + perm[i:]
        return set(tuple(val) for val in all_perms(nums))
    
    # 356 ms, 20.40%
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, sofar=[]):
            if not nums:
                return [sofar]
            rv = []
            for i in range(len(nums)):
                rv.extend(dfs(nums[:i] + nums[i + 1:], sofar + [nums[i]]))
            return rv
        return set(tuple(val) for val in dfs(nums))

# @lc code=end

