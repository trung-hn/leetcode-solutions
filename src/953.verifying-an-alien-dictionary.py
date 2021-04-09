#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
# TAGS: Hash Table


class Solution:
    # 40 ms, 85 % O(A). A is all charactesr in words
    def isAlienSorted1(self, words: List[str], order: str) -> bool:
        D = {v: i for i, v in enumerate(order)}

        def is_lt(w1, w2):
            for l1, l2 in zip(w1, w2):
                if D[l1] < D[l2]:
                    return True
                if D[l1] > D[l2]:
                    return False
            return len(w1) <= len(w2)
        return all(is_lt(words[i], words[i+1]) for i in range(len(words) - 1))

    # 36 ms, 97 %. Sort, O(NlogN)
    def isAlienSorted1(self, words: List[str], order: str) -> bool:
        D = {v: i for i, v in enumerate(order)}

        def custom_sort(word):
            return list(map(D.get, word))
        return sorted(words, key=custom_sort) == words

    # 36 ms, 97 % O(A). A is all charactesr in words
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {v: i for i, v in enumerate(order)}
        words = [[index[c] for c in w] for w in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))
# @lc code=end
