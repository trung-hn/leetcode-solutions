#
# @lc app=leetcode id=1859 lang=python3
#
# [1859] Sorting the Sentence
#

# @lc code=start
# TAGS: String, Sorting


class Solution:
    # 24 ms, 94.80%. Time: O(N). Space: O(N)
    def sortSentence(self, s: str) -> str:
        def get_index(word):
            for i, c in enumerate(word):
                if c in "0123456789":
                    return word[:i], word[i:]
        words = s.split()
        answer = [""] * (len(words) + 1)
        for word in words:
            w, index = get_index(word)
            answer[int(index)] = w
        return " ".join(answer[1:])
# @lc code=end
