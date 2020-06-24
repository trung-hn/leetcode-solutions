#
# @lc app=leetcode id=1452 lang=python3
#
# [1452] People Whose List of Favorite Companies Is Not a Subset of Another List
#

# @lc code=start
class Solution:
    """
    There is a better solution with Union Find.
    """

    # 840 ms, 32.77%. Bruteforce. Time: O(N^2), Space: O(N) where N is all counts of companies
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favoriteCompanies = [set(comp) for comp in favoriteCompanies]
        N = len(favoriteCompanies)
        ans = set(range(N))
        for i, set1 in enumerate(favoriteCompanies):
            for j, set2 in enumerate(favoriteCompanies):
                if i == j : continue
                if bool(set1 - set2) == False:
                    if i in ans: ans.remove(i)
        return ans

    # 512 ms. 61.64%. Optimized with sort. Same complexity
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favoriteCompanies = [[i, set(val)] for i, val in enumerate(favoriteCompanies)]
        favoriteCompanies.sort(key=lambda x: len(x[1]))
        N = len(favoriteCompanies)
        ans = set(range(N))
        for i, (i1, set1) in enumerate(favoriteCompanies):
            for i2, set2 in favoriteCompanies[i + 1:]:
                if i1 == i2 : continue
                if bool(set1 - set2) == False:
                    if i1 in ans: ans.remove(i1)
        return ans
    
# @lc code=end

