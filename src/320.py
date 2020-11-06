# TAGS: Premium, Backtracking
class Solution:
    # 144 ms, 92.57%. Time: O(N*2^N). Space: O(N)
    def generateAbbreviations(self, word: str) -> List[str]:
        self.ans = []
        def dfs(word, sofar=''):
            if not word:
                self.ans.append(sofar)
                return
            for i in range(len(word) + 1):
                if i == 0:
                    dfs(word[i+1:], sofar + word[i])
                else:
                    dfs(word[i+1:], sofar + str(i) + word[i:i+1])
        dfs(word)
        return self.ans