#
# @lc app=leetcode id=1583 lang=python3
#
# [1583] Count Unhappy Friends
#

# @lc code=start
# TAGS: Array
import collections, itertools
class Solution:
    # 364 ms, 99.79%. Time: O(N^2). Space: O(N^2)
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        wanted_friends = collections.defaultdict(set)
        for p1, p2 in pairs:
			# in Layman's terms, take every number until we find p in the preferences (linear fashion)
            wanted_friends[p1] = set(itertools.takewhile(lambda p: p!=p2 , preferences[p1]))
            wanted_friends[p2] = set(itertools.takewhile(lambda p: p!=p1 , preferences[p2]))
        
		# For the given example, we will have wanted_friends as follows:
		# {0: set(), 1: {2, 3}, 2: set(), 3: {1}}
		# This means, 0 and 2 are happy, 1 wants 2 or 3, and 3 wants 1. 
		
        unhappy_friends = 0
        for curr, people in wanted_friends.items():
            if any(curr in wanted_friends[person] for person in people):
                unhappy_friends += 1
        return unhappy_friends
# @lc code=end

