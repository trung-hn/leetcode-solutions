#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#

# @lc code=start
# TAGS: Hash Table, Dynamic Programming


class Solution:

    # Time: O(NlogN + N*N*C)
    def longestStrChain(self, words: List[str]) -> int:
        def is_match(word, option):
            if word == "":
                return True
            i = j = cnt = 0
            while i < len(word) and j < len(option):
                if word[i] == option[j]:
                    i += 1
                else:
                    cnt += 1
                j += 1
            return cnt <= 1

        # Sort from longest to shortest
        words.sort(key=len)
        words_by_len = collections.defaultdict(list)
        for word in words:
            words_by_len[len(word)].append(word)

        longest_chain = collections.defaultdict(int)
        longest_chain[''] = 0

        # Try all pairs and check if it is valid
        for word in words:
            for option in words_by_len[len(word) + 1]:
                if is_match(word, option):
                    longest_chain[option] = max(
                        longest_chain[option], longest_chain[word] + 1)
        return max(longest_chain.values()) + 1

    # 132 ms, 71.74%. Time: O(N*logN + N*C*C). Space: O(N)
    def longestStrChain(self, words: List[str]) -> int:
        # Search Space
        available = set(words)

        # Sort from longest to shortest
        words.sort(key=len, reverse=True)
        longest_chain = collections.defaultdict(int)
        longest_chain[''] = 0

        # Try all combinations and check if it is in available
        for word in words:
            for i in range(len(word)):
                new = word[:i] + word[i + 1:]
                if new not in available:
                    continue
                longest_chain[new] = max(
                    longest_chain[new], longest_chain[word] + 1)
        return max(longest_chain.values()) + 1
# @lc code=end
