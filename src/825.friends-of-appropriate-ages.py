#
# @lc app=leetcode id=825 lang=python3
#
# [825] Friends Of Appropriate Ages
#

# @lc code=start
# TAGS: Array
import bisect
import collections
class Solution:
    # 420 ms, 21.22%. Time: O(NlogN). Space: O(N)
    def numFriendRequests(self, ages: List[int]) -> int:
        def bisect_left(ages, target):
            lo, hi = 0, len(ages) - 1
            while lo < hi:
                mid = (hi - lo) // 2 + lo
                if ages[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        
        def bisect_right(ages, target):
            lo, hi = 0, len(ages) - 1
            while lo < hi:
                mid = hi - (hi - lo) // 2
                if ages[mid] <= target:
                    lo = mid
                else:
                    hi = mid - 1
            return lo + 1
        
        ans = 0
        ages.sort()
        for i, age in enumerate(ages):
            upper_age = age
            lower_age = age // 2 + 8
            if upper_age < lower_age:
                continue
            i1 = bisect.bisect_left(ages, lower_age)
            i2 = bisect.bisect_right(ages, upper_age) - 1
            ans += i2 - i1
        return ans
    
    # 712ms, 8.9%. Time: O(N). Space: O(1). because age < 120
    def numFriendRequests(self, ages: List[int]) -> int:
        counter = collections.Counter(ages)
        ans = 0
        for age in ages:
            upper_age = age
            lower_age = age // 2 + 8
            if upper_age < lower_age: continue
            ans += sum(counter[a] for a in range(lower_age, upper_age + 1)) - 1
        return ans

# @lc code=end

