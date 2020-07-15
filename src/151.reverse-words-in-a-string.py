#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
# TAGS: String
class Solution:
    # Time and Space: O(N)
    def reverseWords(self, s: str) -> str:
        start_i = 0
        s = " " + s + " "
        lst = []
        for i, c in enumerate(s):
            # if prev=" " and current!=" " then it is the start of a word
            if s[i-1] == " " and c != " ":
                start_i = i
            # if current=" " and prev!=" " then it is the end of a word
            elif c == " " and s[i-1] != " ":
                lst.append(s[start_i : i + 1].strip())
        return " ".join(reversed(lst))
                
            
    # Time and Space: O(N)
    def reverseWords(self, s:str) -> str:
        words = s.split()
        return " ".join(reversed(words))
# @lc code=end

