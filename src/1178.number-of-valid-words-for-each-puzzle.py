#
# @lc app=leetcode id=1178 lang=python3
#
# [1178] Number of Valid Words for Each Puzzle
#

# @lc code=start

# TAGS: Array, Hash Table, String, Bit Manipulation, Trie
class Solution:
    # LTE
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def check_against(word, store, freq):
            word = set(word)
            for st, add in store.items():
                if len(word - set(st)) <= 1:
                    for a in add:
                        ans[a] += freq

        words = [''.join(sorted(set(word))) for word in words]
        freq = collections.Counter(words)

        store = collections.defaultdict(lambda: collections.defaultdict(list))
        for puzzle in puzzles:
            c, *rest = puzzle
            order = ''.join(sorted(rest))
            store[c][order].append(puzzle)

        ans = collections.defaultdict(int)
        for word, fq in freq.items():
            for c in word:
                if c in store:
                    check_against(word, store[c], fq)

        return [ans[p] for p in puzzles]

    # 504 ms, 95.28%. From article
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:

        def bitmask(word: str) -> int:
            mask = 0
            for letter in word:
                mask |= 1 << (ord(letter) - ord('a'))
            return mask

        # Create a bitmask for each word.
        word_count = Counter(bitmask(word) for word in words)

        result = []
        for puzzle in puzzles:
            first = 1 << (ord(puzzle[0]) - ord('a'))
            count = word_count[first]

            # Make bitmask but ignore the first character since it must always
            # be there.
            mask = bitmask(puzzle[1:])

            # Iterate over every possible subset of characters.
            submask = mask
            while submask:
                # Increment the count by the number of words that match the
                # current submask.
                count += word_count[submask | first]  # add first character
                submask = (submask - 1) & mask
            result.append(count)
        return result
# @lc code=end
