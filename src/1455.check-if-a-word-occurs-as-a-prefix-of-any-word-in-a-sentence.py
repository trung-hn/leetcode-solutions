#
# @lc app=leetcode id=1455 lang=python3
#
# [1455] Check If a Word Occurs As a Prefix of Any Word in a Sentence
#

# @lc code=start
# TAGS: String, Pythonic
class Solution:
    # 20 ms, 99.06%. Time: O(N), Space: O(1)
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for i, word in enumerate(words):
            if len(word) < len(searchWord): continue
            if word[:len(searchWord)] == searchWord:
                return i + 1
        return -1

    # 20 ms, 99.06%. Pythonic. Time: O(N), Space: O(1)
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split()):
            if word.startswith(searchWord):
                return i + 1
        return -1
# @lc code=end

