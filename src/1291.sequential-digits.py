#
# @lc app=leetcode id=1291 lang=python3
#
# [1291] Sequential Digits
#

# @lc code=start
# TAGS: Backtracking
class Solution:
    """
    No Backtracking is used here: Backtracking can be done with DFS
    """
    # 16 ms, 99%.
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        numbers = list(map(str, range(1,10)))
        ans = []
        for num_len in range(len(str(low)), len(str(high)) + 1):
            start = 0
            end = start + num_len
            while end != 10:
                number = int("".join(numbers[start : end]))
                if low <= number <= high:
                    ans.append(number)
                start += 1
                end += 1
        return ans
    
    # 20 ms, 97%. 
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        numbers = list(map(str, range(1,10)))
        ans = []
        for num_len in range(len(str(low)), len(str(high)) + 1):
            start = 0
            for end in range(start + num_len, 10):
                number = int("".join(numbers[start : end]))
                if low <= number <= high:
                    ans.append(number)
                start += 1
        return ans
    
    # 32 ms, 90%. 
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        numbers = list("0123456789")
        ans = []
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(1, 10):
                end = start + length
                if end > 10: break
                number = int(''.join(numbers[start : end]))
                if low <= number <= high:
                    ans.append(number)  
        return ans
# @lc code=end

