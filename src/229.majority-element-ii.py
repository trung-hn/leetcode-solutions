#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
# TAGS: Array
# REVIEWME: Voting Algorithm. 
class Solution:
    # Time and Space: O(N)
    def majorityElement(self, nums: List[int]) -> List[int]:
        D = {}
        for num in nums:
            D[num] = D.get(num, 0) + 1
        ans = []
        for k, v in D.items():
            if v > len(nums)/3: ans.append(k)
        return ans
    
    # Time and Space: O(N)
    def majorityElement(self, nums: List[int]) -> List[int]:
        D = {}
        for num in nums:
            D[num] = D.get(num, 0) + 1
        ans = []
        for k, v in D.items():
            if v > len(nums)/3: ans.append(k)
        return ans
    
    # Time: O(N). Space: O(1). From solution article
    # Voting Algorithm
    def majorityElement(self, nums):
        if not nums:
            return []
        
        # 1st pass
        count1, count2, candidate1, candidate2 = 0, 0, None, None
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        # 2nd pass
        result = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums)//3:
                result.append(c)

        return result
    
    # Time: O(N). Space: O(1). Revise. 
    # Voting Algorithm
    def majorityElement(self, nums):
        candidates = [0, 0]
        freq = [0, 0]
        for num in nums:
            if num in candidates:
                index = candidates.index(num)
                freq[index] += 1
            elif 0 in freq:
                index = freq.index(0)
                candidates[index] = num
                freq[index] += 1
            else:
                freq[0] -= 1
                freq[1] -= 1
        return set(c for c in candidates if nums.count(c) > len(nums) // 3)  
# @lc code=end

