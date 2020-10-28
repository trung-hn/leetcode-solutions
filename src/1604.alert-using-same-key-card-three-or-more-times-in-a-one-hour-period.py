#
# @lc app=leetcode id=1604 lang=python3
#
# [1604] Alert Using Same Key-Card Three or More Times in a One Hour Period
#

# @lc code=start
# TAGS: String, Ordered Map
class Solution:
    # 668 ms, 99.52%. Time: O(NlogN). Space: O(N)
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        def is_within_1hr(t1, t2):
            h1, m1 = t1.split(":")
            h2, m2 = t2.split(":")
            if int(h1) + 1 < int(h2): return False
            return h1 == h2 or m1 >= m2
        
        records = collections.defaultdict(list)
        for name, time in zip(keyName, keyTime):
            records[name].append(time)
        
        rv = []
        for person, record in records.items():
            record.sort()
            if any(is_within_1hr(t1, t2) for t1, t2 in zip(record, record[2:])):
                rv.append(person)
        return sorted(rv)
                     
# @lc code=end

