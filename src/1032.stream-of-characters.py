#
# @lc app=leetcode id=1032 lang=python3
#
# [1032] Stream of Characters
#

# @lc code=start
import collections
class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.end = None
    def __repr__(self):
        return f"children: {self.children}, end: {self.end}"

class StreamChecker:
    """
    This works but TLE
    """
    def __init__(self, words: List[str]):
        # Create a Trie
        # Init a dictionary where key is a sequence, value is a Trie
            # "" : original Trie

        self.head = Trie()
        for word in words:
            head = self.head
            for c in word:
                head = head.children[c]
            head.end = True
        self.dict = {"" : self.head}

    def query(self, letter: str) -> bool:
        # flag = False
        # for each sequence in dictionary:
            # sequence += letter
            # check if new sequence follow the Trie
                # if Yes -> flag = True
            # If child Trie exists -> add new pair: {new sequence : new child Trie}
            # Remove old pair
        # return flag
        # print(self.dict)

        rv = False
        visited = set()
        for seq in list(self.dict.keys()):
            trie = self.dict[seq]
            if letter in trie.children:
                self.dict[seq + letter] = trie.children[letter]
                visited.add(seq + letter)
                if trie.children[letter].end:
                    rv = True
            if seq not in visited and seq != "":
                del self.dict[seq]
        return rv

class StreamChecker:
    """
    Similar to above but cleaner. LTE
    """
    def __init__(self, words: List[str]):
        self.head = Trie()
        for word in words:
            head = self.head
            for c in word:
                head = head.children[c]
            head.end = True
        self.tries = []

    def query(self, letter: str) -> bool:
        self.tries = [seq.children[letter] for seq in self.tries + [self.head] if letter in seq.children]
        return any(trie.end for trie in self.tries)


class StreamChecker:
    """
    Inspired from lee215: https://leetcode.com/problems/stream-of-characters/discuss/278250/Python-Trie-Solution-with-Explanation
    Very similar to the solution above. But we reverse the words to speed up cases like this: "ab" vs "aaaaab"
    Time and Space: O(M), where M is a max word length, i.e. the depth of trie.
    """
    def __init__(self, words: List[str]):
        self.head = Trie()
        for word in words:
            head = self.head
            for c in word[::-1]:
                head = head.children[c]
            head.end = True
        self.S = ""
    def query(self, letter: str) -> bool:
        self.S = letter + self.S
        trie = self.head
        for c in self.S:
            if c in trie.children:
                trie = trie.children[c]
                if trie.end: return True
            else:
                break
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
# @lc code=end

